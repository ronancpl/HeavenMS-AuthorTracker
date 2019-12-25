from authortrackprocessor import AuthorTrackRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.patrons import AuthorPatronType
from authorscanner.patrons import AuthorPatronFeatType

contrib_feat_type = {AuthorPatronType.AuthorPatronType.AUTHBY: AuthorPatronFeatType.FeatType.CODE_AUTHBY,
                     AuthorPatronType.AuthorPatronType.AUTHOR: AuthorPatronFeatType.FeatType.CODE_AUTHOR,
                     AuthorPatronType.AuthorPatronType.CONTRB: AuthorPatronFeatType.FeatType.CODE_CONTRB}

contrib_directory_feat_type = {AuthorPatronType.AuthorPatronType.AUTHBY: AuthorPatronFeatType.FeatType.CODE_AUTHBY_DIRECTORY,
                               AuthorPatronType.AuthorPatronType.AUTHOR: AuthorPatronFeatType.FeatType.CODE_AUTHOR_DIRECTORY,
                               AuthorPatronType.AuthorPatronType.CONTRB: AuthorPatronFeatType.FeatType.CODE_CONTRB_DIRECTORY}


def countPatronCodeActivity(patron_name, commit_timesection):
    # git patron movement here will be used only to track assiduity

    for patron in patronManager.getPatron(patron_name):
        patron.addTimesetActivity(commit_timesection, True)


def countPatronFileContribution(patron_activity_table, patron_contrib_type, file_path, contrib_count):
    if file_path not in patron_activity_table[patron_contrib_type]:
        patron_activity_table[patron_contrib_type][file_path] = contrib_count
    else:
        patron_activity_table[patron_contrib_type][file_path] += contrib_count


def countPatronContribution(commit_patrons_activity, patron_name, timesection, limit_timesection, file_path, contribution_type, patron_count):
    if patron_name not in commit_patrons_activity:
        patron_activity = []
        for i in range(limit_timesection):
            patron_activity_item = {}
            patron_activity_item[AuthorPatronType.AuthorPatronType.AUTHBY] = {}
            patron_activity_item[AuthorPatronType.AuthorPatronType.AUTHOR] = {}
            patron_activity_item[AuthorPatronType.AuthorPatronType.CONTRB] = {}

            patron_activity.append(patron_activity_item)

        commit_patrons_activity[patron_name] = patron_activity
    else:
        patron_activity = commit_patrons_activity[patron_name]

    countPatronFileContribution(patron_activity[timesection], contribution_type, file_path, patron_count)


def fetchPatronsSourceCodeDirectoryActivity(commit_patrons_db, max_timesection):
    commit_patrons_activity = {}

    commit_timesection = 0
    for commit_patrons_range in commit_patrons_db:  # not using simple tracker on this one, since it doesn't track timestamp
        for commit_patron in commit_patrons_range:
            for commit_file_path, commit_file_patrons in commit_patron['diff'].items():
                for file_patron_type, file_patron_items in commit_file_patrons.items():
                    for file_patron_name, file_patron_count in file_patron_items.items():
                        countPatronCodeActivity(file_patron_name, commit_timesection)
                        countPatronContribution(commit_patrons_activity, file_patron_name, commit_timesection, max_timesection, commit_file_path, file_patron_type, file_patron_count)

        commit_timesection += 1

    return commit_patrons_activity


def getDirectoryNameFromFilePath(file_path, max_depth):
    try:
        return '/'.join(file_path.split('/', max_depth)[:-1])
    except:
        return ''


def createPatronDirectoryActivity():
    ret = {}

    for contrib_feat_type in contrib_directory_feat_type.keys():
        ret[contrib_feat_type] = {}

    return ret


def filterPatronsSourceCodeDirectoryActivity(file_patrons_activity, limit_timesection):
    # generate a table to recollect directories a patron had been working on
    max_depth = 2

    directory_patrons_activity = {}

    for patron_name, patron_data in file_patrons_activity.items():
        if patron_name not in directory_patrons_activity:
            patron_activity = []
            for i in range(limit_timesection):
                patron_activity_item = createPatronDirectoryActivity()
                patron_activity.append(patron_activity_item)

            directory_patrons_activity[patron_name] = patron_activity
        else:
            patron_activity = directory_patrons_activity[patron_name]

        i = 0
        for patron_timesection_data in patron_data:
            for patron_contrib_type, patron_contrib_data in patron_timesection_data.items():
                for file_path, file_count in patron_contrib_data.items():
                    countPatronFileContribution(patron_activity[i], patron_contrib_type, getDirectoryNameFromFilePath(file_path, max_depth), file_count)

            i += 1

    return directory_patrons_activity


def processPatronsSourceCodeActivity():
    commit_patrons_db = tracker.source2
    max_timesection = len(commit_patrons_db)

    commit_patrons_activity = fetchPatronsSourceCodeDirectoryActivity(commit_patrons_db, max_timesection)
    directory_patrons_activity = filterPatronsSourceCodeDirectoryActivity(commit_patrons_activity, max_timesection)

    return commit_patrons_activity, directory_patrons_activity


def scorePatronActivity(patron, patron_activity, patron_directory_activity):
    i = 0
    for patron_timesection in patron_activity:
        patron_activity_count = {
            AuthorPatronType.AuthorPatronType.AUTHBY: 0,
            AuthorPatronType.AuthorPatronType.AUTHOR: 0,
            AuthorPatronType.AuthorPatronType.CONTRB: 0
        }

        for patron_type, patron_type_activity in patron_timesection.items():
            for patron_file, patron_count in patron_type_activity.items():
                patron_activity_count[patron_type] += patron_count

        for patron_type, patron_count in patron_activity_count.items():
            if patron_count > 0:
                patron.addFeat(contrib_feat_type[patron_type], patron_count, i, True)

        i += 1

    i = 0
    for patron_timesection in patron_directory_activity:
        patron_activity_count = {
            AuthorPatronType.AuthorPatronType.AUTHBY: 0,
            AuthorPatronType.AuthorPatronType.AUTHOR: 0,
            AuthorPatronType.AuthorPatronType.CONTRB: 0
        }

        for patron_type, patron_type_activity in patron_timesection.items():
            for patron_dir, patron_count in patron_type_activity.items():
                patron_activity_count[patron_type] += patron_count

        for patron_type, patron_count in patron_activity_count.items():
            if patron_count > 0:
                patron.addFeat(contrib_directory_feat_type[patron_type], patron_count, i, True)

        i += 1


def scoreSourceCode():
    global tracker
    tracker = AuthorTrackRepository.tracker

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    commit_patrons_activity, directory_patrons_activity = processPatronsSourceCodeActivity()

    for patron_name in directory_patrons_activity.keys():
        for patron in patronManager.getPatron(patron_name):
            scorePatronActivity(patron, commit_patrons_activity[patron_name], directory_patrons_activity[patron_name])


def run():
    scoreSourceCode()


if __name__ == '__main__':
    run()
