from enum import Enum

from authorscanner import AuthorScanRepository


class ResultFile(Enum):
    WORLDMAP = 'worldmap/worldmap_movement.txt'
    ATOMIC_DIRECTORY = 'project/atomic/directory_modification_count.txt'
    ATOMIC_FILE = 'project/atomic/file_modification_count.txt'
    COMMIT_FILE_LINE_GROWTH = 'project/commit/file_line_growth.txt'
    COMMIT_FILE_SIZE_GROWTH = 'project/commit/file_size_growth.txt'
    CONTENT_ACCEPTED_PULL_REQUESTS = 'project/content/accepted_pull_requests.txt'
    CONTENT_FILE_COUNT_GROWTH = 'project/content/file_count_growth.txt'
    CONTENT_FILE_SIZE_GROWTH = 'project/content/file_size_growth.txt'
    CONTENT_RELEASE_GROWTH = 'project/content/release_growth.txt'
    CONTENT_REPOSITORY_GROWTH = 'project/content/repository_growth.txt'
    CONTENT_REPOSITORY_KEYWORD = 'project/content/repository_keywords.txt'
    CONTENT_REPOSITORY_LOG_KEYWORD = 'project/content/repository_log_keywords.txt'
    CONTENT_SEARCHED_PATHS = 'project/content/searched_paths.txt'
    TRAFFIC_CLONES = 'project/traffic/clones.txt'
    TRAFFIC_PATHS = 'project/traffic/paths.txt'
    TRAFFIC_REFERRERS = 'project/traffic/referrers.txt'
    TRAFFIC_VIEWS = 'project/traffic/views.txt'
    CREATOR_COMMIT_FREQUENCY = 'project/creator/commit_frequency.txt'
    CREATOR_COMMIT_GRAPH_ACTIVITY = 'project/creator/commit_activity.txt'
    CREATOR_COMMIT_GRAPH_AVG_TIME = 'project/creator/average_time.txt'
    CREATOR_ISSUES_CLOSED = 'project/creator/issues_closed.txt'
    CREATOR_LINE_GROWTH = 'project/creator/line_growth.txt'
    PATRONS_SCORE = 'patrons/patron_scores.txt'
    PATRONS_WORD = 'patrons/patron_words.txt'
    PATRONS_WORD_UNIT = 'patrons/patron/words.txt'
    SURVEY_QUESTION = 'survey/survey_questions.txt'
    SURVEY_TABLE = 'survey/survey_table.txt'


    def readGraphFile(self):
        global scanner
        scanner = AuthorScanRepository.scanner

        return scanner.readGraphFile(self.value)
