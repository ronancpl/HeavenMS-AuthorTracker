from authorscanner.patrons import AuthorPatronFeatType
from authortrackscorer import AuthorScoreHolder
from authorconstants import AuthorConstantLimit

import inspect

social_feat_types = [AuthorPatronFeatType.FeatType.SOCIAL_CHARACTER,
                         AuthorPatronFeatType.FeatType.SOCIAL_QUESTION,
                         AuthorPatronFeatType.FeatType.SOCIAL_CODE]

class AuthorPatronElement:

    def initializeStats(self, patron_name):
        patron_stats = {}
        patron_stats["login"] = patron_name
        patron_stats["custom_image"] = None
        patron_stats["nationality"] = None
        patron_stats["public_repos"] = 0
        patron_stats["public_gists"] = 0

        return patron_stats


    def __init__(self, name, aliases, nationality, stats):
        self.assiduity = set()
        self.score = None

        self.authorship_feats = {}
        self.score_feats = {}
        self.social_tourist = True

        self.name = name
        self.aliases = aliases
        self.nationality = nationality

        self.stats = self.initializeStats(name)
        self.stats.update(stats)

        self.authorship_feats[AuthorPatronFeatType.FeatType.CODE_AUTHOR] = {}
        self.authorship_feats[AuthorPatronFeatType.FeatType.CODE_AUTHBY] = {}
        self.authorship_feats[AuthorPatronFeatType.FeatType.CODE_CONTRB] = {}


    def __str__(self):
        return '`' + self.name + ' ' + str(self.aliases) + ' from ' + str(self.nationality) + ' has assiduity ' + str(self.assiduity) + ' ' + ' and actions ' + str(self.score_feats) + '`' + ' | Tourist: ' + str(self.social_tourist)


    def addTimesetActivity(self, feat_timeset, retainer_activity):
        if retainer_activity:
            self.assiduity.add(feat_timeset)


    def addFeat(self, feat_type, feat_count, feat_timeset, retainer_activity):
        if feat_count < 1:
            return

        self.addTimesetActivity(feat_timeset, retainer_activity)

        if feat_type in self.score_feats:
            self.score_feats[feat_type] += feat_count
        else:
            self.score_feats[feat_type] = feat_count


    def getFeat(self, feat_type):
        if feat_type in self.score_feats:
            return self.score_feats[feat_type]
        else:
            return 0


    def calcScore(self):
        global scorer
        scorer = AuthorScoreHolder.scorer

        self.score_feats[AuthorPatronFeatType.FeatType.ASSIDUITY] = len(self.assiduity)

        self.score = 0.0
        self.social_tourist = True
        for feat_type, feat_count in self.score_feats.items():
            self.score += (scorer.score[feat_type] * feat_count)

        if self.score > 0.0:
            non_social_feats = self.score_feats.copy()

            for f in social_feat_types:
                if f in non_social_feats:
                    non_social_feats.pop(f)

            if len(non_social_feats) > 1:
                self.social_tourist = False
            else:
                chr_count = 0
                chr_count += self.getFeat(AuthorPatronFeatType.FeatType.SOCIAL_CHARACTER)
                chr_count += self.getFeat(AuthorPatronFeatType.FeatType.SOCIAL_QUESTION)
                chr_count += self.getFeat(AuthorPatronFeatType.FeatType.SOCIAL_CODE)

                print('Only social feats from ' + self.name + ' | chars: ' + str(chr_count))

                if chr_count >= AuthorConstantLimit.WrapLimit.PATRON_DISTINGUISHED_CHAT_COUNT.getValue():
                    self.social_tourist = False


    def exportScore(self):
        patron_dict = {}
        str_dict = ''

        for n, v in sorted(inspect.getmembers(self), key=lambda k:k[0]):  # src: https://stackoverflow.com/questions/3818825/python-what-is-the-correct-way-to-copy-an-objects-attributes-over-to-another/3818861
            try:
                if type(v) is dict: # dict-types shouldn't get exported
                    continue

                patron_dict[n] = v
                str_dict += str(n) + ', '
            except AttributeError:
                pass

        return patron_dict


def createPatron(name, aliases, nationality, stats):
    return AuthorPatronElement(name, aliases, nationality, stats)
