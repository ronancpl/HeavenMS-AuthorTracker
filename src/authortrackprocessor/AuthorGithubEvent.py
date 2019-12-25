github_event_metadata = {
    'CreateEvent' : ('ref_type', {'repository': 'repo_create_count', 'branch': 'branch_create_count'}),
    'CommitCommentEvent' : ('action', {'created': 'comment_count'}),
    'IssueCommentEvent' : ('action', {'created': 'comment_count'}),
    'ContentReferenceEvent' : ('action', {'created': 'content_ref_count'}),
    'ForkEvent' : ('*', {'': 'fork_create_count'}),
    'GistEvent' : ('action', {'create': 'gist_create_count'}),
    'GollumEvent' : ('*', {'': 'wiki_update_count'}),
    'IssuesEvent' : ('action', {'opened': 'issue_create_count'}),
    'PullRequestEvent' : ('action', {'opened': 'pull_create_count'}),
    'PushEvent' : ('*', {'': 'branch_push_create_count'}),
    'ReleaseEvent' : ('*', {'': 'release_create_count'}),
    'RepositoryEvent' : ('action', {'created': 'repo_create_count'}),
    'WatchEvent' : ('action', {'started': 'stargaze_count'})
}

github_event_entries = set()
for event_entry in github_event_metadata.values():
    for event_entry_item in event_entry[1].values():
        github_event_entries.add(event_entry_item)