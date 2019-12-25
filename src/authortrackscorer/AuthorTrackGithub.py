from authortrackprocessor import AuthorTrackRepository
from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.patrons import AuthorPatronFeatType

import math


def scoreSingleActivity(github_patron, patron_type, patron_count, patron_timesection):
    if patron_count is None:
        print('Error: ' + str(patron_type.name) + ' has none count on "' + github_patron.name + '"')
        return

    if patron_count > 0:
        if patron_timesection is not None:
            patron_ts = patron_timesection
        else:
            patron_ts = -1

        github_patron.addFeat(patron_type, patron_count, patron_ts, True)


def scoreAttributeActivity(github_patron, stat_activities, feat_type):
    i = 0
    for ts_activity_count in stat_activities:
        github_patron.addFeat(feat_type, ts_activity_count, i, True)
        i += 1


def fetchRepositoryTimeSectionFromActivity(github_item):
    return scanner.fetchRepositoryTimeSectionFromTimestamp(github_item['created_at'], days=20)


def recalledPullCommitsPenalty(github_pull):
    if github_pull['number'] not in scanner.recalled_pulls:
        return None

    additions = 0
    deletions = 0
    changes = 0
    changed_files = 0

    for pull_commit_req in github_pull['commits']:
        for pull_commit in pull_commit_req:
            commit_sha = pull_commit['sha']
            if commit_sha not in scanner.recalled_commits:
                commit_data = scanner.commits[commit_sha]

                stats_additions = commit_data['stats']['additions']
                stats_deletions = commit_data['stats']['deletions']

                commit_additions = 0
                commit_deletions = 0
                if stats_additions > stats_deletions:
                    commit_additions = stats_additions - stats_deletions
                    commit_changes = stats_deletions
                else:
                    commit_deletions = stats_deletions - stats_additions
                    commit_changes = stats_additions

                commit_changed_files = len(commit_data['files'])

                additions += commit_additions
                deletions += commit_deletions
                changed_files += commit_changed_files
                changes += commit_changes

    return [additions, deletions, changes, changed_files]


def calcNonMergedActivityCount(count):
    if count > 0:
        return math.ceil(math.log(count, 1.7))
    else:
        return 0


def scorePatronActivities(github_patron, patron_entry):
    github_patron.stats['comment_character_count_ts'] = [0] * scanner.tracker_timesection_len
    github_patron.stats['comment_directory_path'] = {}

    github_patron.stats['pull_commit_count_ts'] = [0] * scanner.tracker_timesection_len
    github_patron.stats['pull_additions_count_ts'] = [0] * scanner.tracker_timesection_len
    github_patron.stats['pull_deletions_count_ts'] = [0] * scanner.tracker_timesection_len
    github_patron.stats['pull_changes_count_ts'] = [0] * scanner.tracker_timesection_len
    github_patron.stats['pull_changed_files_count_ts'] = [0] * scanner.tracker_timesection_len

    scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_USER_REPOS, patron_entry["repo_count"], None)
    scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_USER_FORKS, patron_entry["fork_count"], None)

    scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_USER_PROFILE_IMAGE, 1 if patron_entry["custom_image"] else 0, None)
    scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_USER_LOCALITY, 1 if patron_entry["nationality"] is not None else 0, None)

    # patron_entry["public_repos"]    # same as repo_count + fork_count
    scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_USER_GISTS, patron_entry["public_gists"], None)

    forks_ts = set()
    for github_item in patron_entry['main_forks']:
        github_ts = fetchRepositoryTimeSectionFromActivity(github_item)
        scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_FORK, 1, github_ts)
        forks_ts.add(github_ts)

    for github_ts in forks_ts:
        scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_FORK_FRESH, 1, github_ts)

    for github_item in patron_entry['main_stargaze']:
        github_ts = fetchRepositoryTimeSectionFromActivity(github_item)
        scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_STARGAZE, 1, github_ts)

    for github_item in patron_entry['main_watch']:
        github_ts = fetchRepositoryTimeSectionFromActivity(github_item)
        scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_WATCH, 1, github_ts)

    for github_item in patron_entry['main_issues']:
        github_ts = fetchRepositoryTimeSectionFromActivity(github_item)
        scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_ISSUES, 1, github_ts)

        github_patron.stats['comment_character_count_ts'][github_ts] += len(github_item['title']) + len(github_item['body'])

    for github_item in patron_entry['main_pulls']:
        github_ts = fetchRepositoryTimeSectionFromActivity(github_item)
        scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_PULL_REQUESTS, 1, github_ts)

        github_patron.stats['comment_character_count_ts'][github_ts] += len(github_item['title']) + len(github_item['body'])
        github_patron.stats['pull_commit_count_ts'][github_ts] += len(github_item['commits'])

        additions = 0
        deletions = 0
        if github_item['additions'] > github_item['deletions']:
            additions = github_item['additions'] - github_item['deletions']
            changes = github_item['deletions']
        else:
            deletions = github_item['deletions'] - github_item['additions']
            changes = github_item['additions']

        changed_files = github_item['changed_files']

        if github_item['merged_at'] is not None:
            scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_PULL_REQUESTS_MERGED, 1, github_ts)

            recall_penalty = recalledPullCommitsPenalty(github_item)
            if recall_penalty is not None:
                additions = recall_penalty[0]
                deletions = recall_penalty[1]
                changes = recall_penalty[2]
                changed_files = recall_penalty[3]
        elif github_item['closed_at'] is not None:
            additions = calcNonMergedActivityCount(additions)
            deletions = calcNonMergedActivityCount(deletions)
            changes = calcNonMergedActivityCount(changes)
            changed_files = calcNonMergedActivityCount(changed_files)

        github_patron.stats['pull_additions_count_ts'][github_ts] += additions
        github_patron.stats['pull_deletions_count_ts'][github_ts] += deletions
        github_patron.stats['pull_changes_count_ts'][github_ts] += changes
        github_patron.stats['pull_changed_files_count_ts'][github_ts] += changed_files

    for github_item in patron_entry['main_comments']:
        github_ts = fetchRepositoryTimeSectionFromActivity(github_item)
        scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_COMMENTS, 1, github_ts)

        github_patron.stats['comment_character_count_ts'][github_ts] += len(github_item['body'])
        github_patron.stats['comment_directory_path'][scanner.getDirectoryNameFromFilePath(github_item['path'], 2)] = 1

    scoreSingleActivity(github_patron, AuthorPatronFeatType.FeatType.GITHUB_COMMENT_DIRECTORY, len(github_patron.stats['comment_directory_path']), None)

    scoreAttributeActivity(github_patron, github_patron.stats['comment_character_count_ts'], AuthorPatronFeatType.FeatType.GITHUB_COMMENT_CHARACTERS)

    scoreAttributeActivity(github_patron, github_patron.stats['pull_commit_count_ts'], AuthorPatronFeatType.FeatType.GITHUB_PULL_CONTENTS_COMMITS)
    scoreAttributeActivity(github_patron, github_patron.stats['pull_additions_count_ts'], AuthorPatronFeatType.FeatType.GITHUB_PULL_CONTENTS_ADDITIONS)
    scoreAttributeActivity(github_patron, github_patron.stats['pull_deletions_count_ts'], AuthorPatronFeatType.FeatType.GITHUB_PULL_CONTENTS_DELETIONS)
    scoreAttributeActivity(github_patron, github_patron.stats['pull_changes_count_ts'], AuthorPatronFeatType.FeatType.GITHUB_PULL_CONTENTS_CHANGES)
    scoreAttributeActivity(github_patron, github_patron.stats['pull_changed_files_count_ts'], AuthorPatronFeatType.FeatType.GITHUB_PULL_CONTENTS_CHANGED_FILES)


def processGithubActivities():
    for github_patron_name, github_item in tracker.github.items():
        for github_patron in patronManager.getPatron(github_patron_name):
            scorePatronActivities(github_patron, github_item)


def scoreGithub():
    global scanner
    scanner = AuthorScanRepository.scanner

    global tracker
    tracker = AuthorTrackRepository.tracker

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    processGithubActivities()


def run():
    scoreGithub()


if __name__ == '__main__':
    run()

