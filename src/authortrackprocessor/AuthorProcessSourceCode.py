import AuthorScanJsonReader
from authorscanner import AuthorScanRepository
from authorscanner.patrons import AuthorPatronFeatType
from authorscanner.patrons import AuthorPatronManager
from authorscanner.patrons import AuthorPatronType
import os


source_patron_feat_types = {AuthorPatronType.AuthorPatronType.AUTHOR.value: AuthorPatronFeatType.FeatType.CODE_AUTHOR,
                            AuthorPatronType.AuthorPatronType.AUTHBY.value: AuthorPatronFeatType.FeatType.CODE_AUTHBY,
                            AuthorPatronType.AuthorPatronType.CONTRB.value: AuthorPatronFeatType.FeatType.CODE_CONTRB}


def getSourcePatronFeatType(patron_type):
    return source_patron_feat_types[patron_type]


def addPatronSourceFeat(patrons_source_feat, patrons_actor_name, patrons_actor_type, patrons_file_path):
    patron_type = getSourcePatronFeatType(patrons_actor_type)
    patrons_source_feat_table = patrons_source_feat[patron_type]

    if patrons_actor_name not in patrons_source_feat_table:
        patrons_actor_entry = {}
        patrons_source_feat_table[patrons_actor_name] = patrons_actor_entry
    else:
        patrons_actor_entry = patrons_source_feat_table[patrons_actor_name]

    if patrons_file_path not in patrons_actor_entry:
        patrons_actor_entry[patrons_file_path] = 1
    else:
        patrons_actor_entry[patrons_file_path] += 1


def authorReadSourcePatrons():
    patrons_source_feats = {}
    for patron_type in AuthorPatronFeatType.FeatType:
        patrons_source_feats[patron_type] = {}


    for patrons_directory_item in scanner.patrons_directory_info:
        for patrons_directory_file in patrons_directory_item:
            patrons_file_path = patrons_directory_file[0]
            patrons_file_content = patrons_directory_file[1]

            for patrons_file_actor in patrons_file_content:
                patrons_actor_name = patrons_file_actor[0][0]
                patrons_actor_type = patrons_file_actor[1]

                addPatronSourceFeat(patrons_source_feats, patrons_actor_name, patrons_actor_type, patrons_file_path)

    return patrons_source_feats


def readSourceContents():
    patrons_source_feats = authorReadSourcePatrons()
    return patrons_source_feats


def fetchSourceContents():
    global scanner
    scanner = AuthorScanRepository.scanner

    global patronManager
    patronManager = AuthorPatronManager.patronManager

    source_contents_db = readSourceContents()
    return source_contents_db


def fetchSourceContentsWithTimestamp():
    global scanner
    scanner = AuthorScanRepository.scanner

    scanner_commit_patrons = scanner.commit_patrons

    commit_patrons_db = scanner.generateTimeSectionDatabase(scanner_commit_patrons.values(), ['created_at'], days=20)
    return commit_patrons_db


def run():
    fetchSourceContents()


if __name__ == '__main__':
    run()
