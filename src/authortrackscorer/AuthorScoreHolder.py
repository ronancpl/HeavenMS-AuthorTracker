from authorscanner.patrons.AuthorPatronFeatType import FeatType

class AuthorScoreHolder:

    def loadScoreValues(self):
        global scorer
        scorer = self

        self.score = {
            FeatType.CODE_AUTHOR: 0.75,
            FeatType.CODE_AUTHBY: 0.75,
            FeatType.CODE_CONTRB: 1.0,
            FeatType.CODE_AUTHOR_DIRECTORY: 14.5,
            FeatType.CODE_AUTHBY_DIRECTORY: 14.5,
            FeatType.CODE_CONTRB_DIRECTORY: 10.5,
            FeatType.SURVEY_BASIC: 20.0,
            FeatType.SURVEY_COMPLETE: 15.5,
            FeatType.SOCIAL_CHARACTER: 0.00028,
            FeatType.SOCIAL_QUESTION: 0.07,
            FeatType.SOCIAL_CODE: 0.1,
            FeatType.GITHUB_USER_REPOS: 3.2,
            FeatType.GITHUB_USER_FORKS: 0.8,
            FeatType.GITHUB_USER_GISTS: 1.1,
            FeatType.GITHUB_USER_COMMITS: 0.3,
            FeatType.GITHUB_USER_PULL_REQUESTS: 0.77,
            FeatType.GITHUB_USER_COMMENTS: 0.4,
            FeatType.GITHUB_USER_PROFILE_IMAGE: 8.0,
            FeatType.GITHUB_USER_LOCALITY: 10.0,
            FeatType.GITHUB_FORK: 0.5,
            FeatType.GITHUB_FORK_FRESH: 8.2,
            FeatType.GITHUB_STARGAZE: 25.5,
            FeatType.GITHUB_WATCH: 21.0,
            FeatType.GITHUB_ISSUES: 3.5,
            FeatType.GITHUB_PULL_REQUESTS: 4.0,
            FeatType.GITHUB_PULL_REQUESTS_MERGED: 8.0,
            FeatType.GITHUB_COMMENTS: 1.2,
            FeatType.GITHUB_COMMENT_CHARACTERS: 0.007,
            FeatType.GITHUB_COMMENT_DIRECTORY: 3.0,
            FeatType.GITHUB_PULL_CONTENTS_COMMITS: 2.1,
            FeatType.GITHUB_PULL_CONTENTS_ADDITIONS: 0.21,
            FeatType.GITHUB_PULL_CONTENTS_DELETIONS: 0.21,
            FeatType.GITHUB_PULL_CONTENTS_CHANGES: 0.21,
            FeatType.GITHUB_PULL_CONTENTS_CHANGED_FILES: 2.8,
            FeatType.ASSIDUITY: 1.77
        }


def loadScoreHolder():
    AuthorScoreHolder().loadScoreValues()


global scorer
scorer = None