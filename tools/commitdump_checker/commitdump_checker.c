/*
    This file is part of the HeavenMS MapleStory Server
    Copyleft (L) 2016 - 2019 RonanLana

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as
    published by the Free Software Foundation version 3 as published by
    the Free Software Foundation. You may not use, modify or distribute
    this program under any other version of the GNU Affero General Public
    License.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
*/

#include <stdbool.h>

#include "commons.c"
#include "commitdump_commons.c"
#include "commitdump_file_date.h"

void performCommitdumpFiles(char *commitdate, CommitDumpFileList *cdfile_existing, CommitDumpFileList *cdfile_searched) {
    char buf[COMMITDUMP_FILES_MAX_PATH_SIZE], bufhash[COMMITDUMP_FILES_MAX_PATH_SIZE];
    HashSet *cdfile_absent = hashset_create();

    // bookkeep cdfilename hash
    StrMap *sm = sm_new(20000);

    // insert labeled commitdump files
    if (cdfile_existing != NULL) {
        resetCommitDumpFileCursor(cdfile_existing);
        while(true) {
            CommitDumpFile *file = readCommitDumpFile(cdfile_existing);
            if (file == NULL) {
                break;
            }

            int hash_cdfile = strhash(file->name);
            sprintf(bufhash, "%d", hash_cdfile);

            if (!sm_put(sm, bufhash, file->name)) {
                printf("ERROR: Couldn't insert filename '%s'.\n", file->name);
            }

            hashset_insert(cdfile_absent, hash_cdfile);
        }
    }

    // remove searched commitdump files
    if (cdfile_searched != NULL) {
        resetCommitDumpFileCursor(cdfile_searched);
        while(true) {
            CommitDumpFile *file = readCommitDumpFile(cdfile_searched);
            if (file == NULL) {
                break;
            }

            int hash_cdfile = strhash(file->name);
            hashset_remove(cdfile_absent, hash_cdfile);
        }
    }

    if (cdfile_absent->count > 0) {
        printf("--------------\nCommit date: %s\n", commitdate);

        int *list = hashset_list(cdfile_absent);
        int i;
        for (i = 0; i < cdfile_absent->count; i++) {
            int hash_cdfile = list[i];
            sprintf(bufhash, "%d", hash_cdfile);

            // dump non-existing searched files
            memset(buf, 0, sizeof(buf));
            sm_get(sm, bufhash, buf, sizeof(buf));

            printf("  %s\n", buf);
        }
        free(list);
    }

    sm_delete(sm);
    hashset_destroy(cdfile_absent);
}

char* getCommitdumpFilePath(char *directory_path, char *cd_commit_file_name, char *file_path_buf) {
    strcpy(file_path_buf, directory_path);
    strcat(file_path_buf, "/");
    strcat(file_path_buf, cd_commit_file_name);
    strcat(file_path_buf, ".txt");

    return file_path_buf;
}

CommitDumpFileList* fetchCommitdumpFilesFromDirectory(char *directory_path, char **filenames, int filenames_size) {
    CommitDumpFileList *commitdumps = (CommitDumpFileList *)malloc(filenames_size * sizeof(CommitDumpFileList));

    char buf[COMMITDUMP_FILES_MAX_PATH_SIZE];
    char *cd_commit_file_name;

    int i = 0;
    while ((cd_commit_file_name = filenames[i]) != NULL) {
        commitdumps[i] = createCommitDumpFileList();
        char *file_path = getCommitdumpFilePath(directory_path, cd_commit_file_name, buf);

        loadCommitdumpFile(&(commitdumps[i]), file_path);
        i++;
    }

    return commitdumps;
}

int runCommitdumpChecker() {
    printf("Loading commit dump dates...\n");

    char *fetch_path = "../../lib/commitfetch", *dump_path = "../../lib/commitdump";
    char **dates = fetchCommitdumpDates(fetch_path, dump_path);
    if (dates == NULL) {
        printf("ERROR: Could not locate 'fetch' or 'dump' directory.");
        return -1;
    }

    printf("Fetching commit dump files...\n");

    int dates_sz = 0;
    while (dates[dates_sz] != NULL) {
        dates_sz++;
    }

    CommitDumpFileList *existing_cdfiles = fetchCommitdumpFilesFromDirectory(dump_path, dates, dates_sz);
    CommitDumpFileList *searched_cdfiles = fetchCommitdumpFilesFromDirectory(fetch_path, dates, dates_sz);

    printf("Filtering missed searches on commit dumps...\n");

    int i;
    for (i = 0; i < dates_sz; i++) {
        performCommitdumpFiles(dates[i], &(existing_cdfiles[i]), &(searched_cdfiles[i]));
    }

    printf("Freeing commit dump resources...\n");

    if (searched_cdfiles != NULL) freeCommitDumpFileList(searched_cdfiles, dates_sz);
    if (existing_cdfiles != NULL) freeCommitDumpFileList(existing_cdfiles, dates_sz);

    freeCommitdumpDates(dates);

    return 0;
}

int main() {
    return runCommitdumpChecker();
}
