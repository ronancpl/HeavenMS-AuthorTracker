from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronManager
from authorscanner.words import AuthorWordManager
from authortrackprocessor import AuthorGithubEvent
from datetime import timedelta


def runEventCount(github_patron_data, github_event, github_subtype, event_keyval):
    if github_subtype in github_event['payload']:
        github_payload_type = github_event['payload'][github_subtype]

        for payload_item, github_patron_item in event_keyval.items():
            if github_payload_type == payload_item:
                github_patron_data[github_patron_item][scanner.fetchRepositoryTimeSectionFromTimestamp(github_event['created_at'], days=20)] += 1
                break
    else:
        for github_patron_item in event_keyval.values():
            github_patron_data[github_patron_item][scanner.fetchRepositoryTimeSectionFromTimestamp(github_event['created_at'], days=20)] += 1
            break


def processGithubEvent(github_patron_data, github_event):
    github_event_type = github_event['type']

    if github_event_type == 'RepositoryEvent':
        return
    elif github_event_type == 'PushEvent':
        github_patron_data['branch_push_create_count'][scanner.fetchRepositoryTimeSectionFromTimestamp(github_event['created_at'], days=20)] += github_event['payload']['distinct_size']
    else:
        if github_event_type in AuthorGithubEvent.github_event_metadata:
            github_event_meta = AuthorGithubEvent.github_event_metadata[github_event_type]
            runEventCount(github_patron_data, github_event, github_event_meta[0], github_event_meta[1])


def assembleGithubRepoEvents(github_patrons):
    for github_patron_item in github_patrons.values():
        for github_event in github_patron_item['events']:
            processGithubEvent(github_patron_item, github_event)

        for github_repo in github_patron_item['repos']:
            if github_repo["fork"]:
                github_patron_item['fork_count'] += 1
            else:
                github_patron_item['repo_count'] += 1


def initializePatronEntry(timesection_len):
    patron_entry = {}

    patron_entry["fork_count"] = 0
    patron_entry["repo_count"] = 0

    for entry_event_table in AuthorGithubEvent.github_event_entries:
        patron_entry[entry_event_table] = [0] * timesection_len

    # activity metadata
    patron_entry['main_forks'] = []
    patron_entry['main_stargaze'] = []
    patron_entry['main_watch'] = []
    patron_entry['main_issues'] = []
    patron_entry['main_pulls'] = []
    patron_entry['main_comments'] = []

    patron_entry['word_table'] = []
    for i in range(timesection_len):
        patron_entry['word_table'].append({})

    return patron_entry


def parseGithubCommentBody(text):
    idx = text.rfind('<notifications@github.com> wrote:\n\n>')
    if idx > -1:
        idx = text.rfind('\n\nOn ')
        if idx > -1:
            text = text[:idx + 1]

    return text


def processWordCount(recurring_keywords, github_comment_body):
    text = parseGithubCommentBody(github_comment_body)
    keyword_list = wordManager.generateWordList(text)
    wordManager.updateKeywordFrequency(recurring_keywords, keyword_list)


def assembleGithubUserEvents(github_patrons):
    default_time = scanner.repository_start_time - timedelta(days=20)
    default_time = default_time.replace(hour = 0, minute = 0, second = 0, microsecond = 0)

    for github_item in scanner.repo.values():
        for patron in patronManager.getPatron(github_item['owner']['login']):
            github_patrons[patron.name]['main_forks'].append({'created_at': github_item['created_at'], 'size': github_item['size']})

    for github_item in scanner.forks.values():
        for patron in patronManager.getPatron(github_item['owner']['login']):
            github_patrons[patron.name]['main_forks'].append({'created_at': github_item['created_at'], 'size': github_item['size']})

    for github_item in scanner.stargazers.values():
        for patron in patronManager.getPatron(github_item['user']['login']):
            github_patrons[patron.name]['main_stargaze'].append({'created_at': github_item['starred_at']})

    for github_item in scanner.subscribers.values():
        for patron in patronManager.getPatron(github_item['login']):
            github_patrons[patron.name]['main_watch'].append({'created_at': default_time})

    for github_item in scanner.users_issues.values():
        for patron in patronManager.getPatron(github_item['user']['login']):
            github_patrons[patron.name]['main_issues'].append({'created_at': github_item['created_at'], 'closed_at': github_item['closed_at'], 'state': github_item['state'], 'title': github_item['title'], 'body': github_item['body']})

    pulls_commits = None
    for pull_commit_item in scanner.users_pulls_commits.values():
        pulls_commits = pull_commit_item[0]['commits']
        break

    for github_item in scanner.users_pulls.values():
        for patron in patronManager.getPatron(github_item['user']['login']):
            github_patrons[patron.name]['main_pulls'].append({'created_at': github_item['created_at'], 'closed_at': github_item['closed_at'], 'merged_at': github_item['merged_at'], 'state': github_item['state'], 'number': github_item['number'], 'title': github_item['title'], 'body': github_item['body'], 'commits': pulls_commits[github_item['number']], 'additions': github_item['additions'], 'deletions': github_item['deletions'], 'changed_files': github_item['changed_files']})

    for github_item in scanner.users_comments.values():
        for github_patron in github_item:
            for patron in patronManager.getPatron(github_patron['user']['login']):
                github_ts = scanner.fetchRepositoryTimeSectionFromTimestamp(github_patron['created_at'], days=20)
                patron_wordlist = github_patrons[patron.name]['word_table'][github_ts]
                processWordCount(patron_wordlist, github_patron['body'])

                github_patrons[patron.name]['main_comments'].append({'created_at': github_patron['created_at'], 'body': github_patron['body'], 'path': ''})

    for github_item in scanner.users_issue_comments.values():
        for github_patron in github_item:
            for patron in patronManager.getPatron(github_patron['user']['login']):
                github_ts = scanner.fetchRepositoryTimeSectionFromTimestamp(github_patron['created_at'], days=20)
                patron_wordlist = github_patrons[patron.name]['word_table'][github_ts]
                processWordCount(patron_wordlist, github_patron['body'])

                github_patrons[patron.name]['main_comments'].append({'created_at': github_patron['created_at'], 'body': github_patron['body'], 'path': github_patron['url']})


def readGithubContents():
    timesection_len = scanner.tracker_timesection_len
    github_patrons = {}

    users_events_repos = scanner.users_events_repos

    for patron_name, patron_content in scanner.patrons_individuals.items():
        patron_data = patron_content.stats
        patron_entry = initializePatronEntry(timesection_len)

        patron_entry["custom_image"] = patron_data["custom_image"]
        patron_entry["nationality"] = patron_data["nationality"]
        patron_entry["public_repos"] = patron_data["public_repos"]
        patron_entry["public_gists"] = patron_data["public_gists"]

        if patron_data["login"] in users_events_repos:
            event_repos = users_events_repos[patron_data["login"]]

            patron_entry["events"] = event_repos["events"]
            patron_entry["repos"] = event_repos["repos"]
        else:
            patron_entry["events"] = []
            patron_entry["repos"] = []

        github_patrons[patron_name] = patron_entry

    assembleGithubRepoEvents(github_patrons)
    assembleGithubUserEvents(github_patrons)

    return github_patrons


def fetchGithubContents():
    global scanner
    scanner = AuthorScanRepository.scanner

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    global wordManager
    wordManager = AuthorWordManager.wordManager


    github_patron_db = readGithubContents()
    return github_patron_db


def run():
    fetchGithubContents()


if __name__ == '__main__':
    run()
