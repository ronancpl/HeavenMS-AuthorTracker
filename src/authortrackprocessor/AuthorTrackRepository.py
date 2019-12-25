from authortrackprocessor import AuthorProcessChatHistory
from authortrackprocessor import AuthorProcessGithubHistory
from authortrackprocessor import AuthorProcessSourceCode
from authortrackprocessor import AuthorProcessSurvey
from authortrackprocessor import AuthorProcessWriteLogHistory

class AuthorTrackRepository:

    def trackRepository(self):
        print('Tracking patronage actions...')
        self.github = AuthorProcessGithubHistory.fetchGithubContents()
        self.social = AuthorProcessChatHistory.fetchSocialContents()
        self.source = AuthorProcessSourceCode.fetchSourceContents() # not really needed
        self.source2 = AuthorProcessSourceCode.fetchSourceContentsWithTimestamp()
        self.survey = AuthorProcessSurvey.fetchSurveyContents()
        self.write_log = AuthorProcessWriteLogHistory.fetchWriteLogContents()


    def __init__(self):
        global tracker
        tracker = self

        self.trackRepository()


global tracker
tracker = None