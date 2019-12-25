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

#include "commitdump_file_date.h"

StrHashMap* fetchCommitdumpDatesFromDirectory(const char *directory_path, char **dir_filenames) {
    if (dir_filenames == NULL) {
        return NULL;
    }

    char buf[COMMITDUMP_FILES_MAX_PATH_SIZE], bufhash[COMMITDUMP_FILES_MAX_PATH_SIZE], cdatebuf[COMMITDUMP_FILES_MAX_PATH_SIZE];
    cdatebuf[14] = 0;   // set null terminator

    HashSet *commit_dates = hashset_create();

    // bookkeep cdfile hash
    StrMap *sm = sm_new(20000);

    char *fname;
    int i = 0;

    int fname_shift = strlen(directory_path) + 1;
    while ((fname = dir_filenames[i]) != NULL) {
        char *commit_date_str = strncpy(cdatebuf, fname + fname_shift, 14);

        int hash_cdfile = strhash(commit_date_str);
        sprintf(bufhash, "%d", hash_cdfile);

        sm_put(sm, bufhash, commit_date_str);
        hashset_insert(commit_dates, hash_cdfile);

        i++;
    }

    StrHashMap *shm = (StrHashMap *)malloc(sizeof(StrHashMap));
    shm->hs = commit_dates;
    shm->sm = sm;

    return shm;
}

void freeStrHashMap(StrHashMap *shm) {
    if (shm != NULL) {
        sm_delete(shm->sm);
        hashset_destroy(shm->hs);

        free(shm);
        shm = NULL;
    }
}

StrHashMap* loadCommitdumpDatesFromDirectory(char *directory_path) {
    char **dir_filenames = loadDirectoryFilenames(directory_path);
    StrHashMap *shm = fetchCommitdumpDatesFromDirectory(directory_path, dir_filenames);
    freeDirectoryFilenames(dir_filenames);

    return shm;
}

char** fetchCommitdumpDates(char *fetch_path, char *dump_path) {
    StrHashMap *fetch_shm = loadCommitdumpDatesFromDirectory(fetch_path);
    StrHashMap *dump_shm = loadCommitdumpDatesFromDirectory(dump_path);

    if (fetch_shm == NULL || dump_shm == NULL) {
        freeStrHashMap(dump_shm);
        freeStrHashMap(fetch_shm);

        return NULL;
    }

    hashset_merge(dump_shm->hs, fetch_shm->hs);

    HashSet *dump_hs = dump_shm->hs;
    StrMap *dump_sm = dump_shm->sm;
    char **dates = (char **)malloc((dump_hs->count + 1) * sizeof(char *));

    char buf[COMMITDUMP_FILES_MAX_PATH_SIZE], bufhash[COMMITDUMP_FILES_MAX_PATH_SIZE];
    int *list = hashset_list(dump_hs);
    int i;
    for (i = 0; i < dump_hs->count; i++) {
        int hash_cd = list[i];
        sprintf(bufhash, "%d", hash_cd);

        sm_get(dump_sm, bufhash, buf, sizeof(buf));
        dates[i] = (char *)malloc((strlen(buf) + 1) * sizeof(char));
        strcpy(dates[i], buf);
    }
    free(list);
    dates[i] = NULL;

    freeStrHashMap(dump_shm);
    freeStrHashMap(fetch_shm);

    return dates;
}

void freeCommitdumpDates(char **dates) {
    if (dates != NULL) {
        char *str;
        int i = 0;
        while ((str = dates[i]) != NULL) {
            free(str);
            i++;
        }

        free(dates);
    }
}
