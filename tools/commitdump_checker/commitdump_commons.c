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

#include <dirent.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>

#include "hashset.c"
#include "strmap.c"
#include "commitdump_file_list.h"

#define COMMITDUMP_FILES_MAX_PATH_SIZE 1000
#define COMMITDUMP_DIRECTORY_MAX_FILES 400
#define FILE_CONTENT_BUCKET_LENGTH 20000
#define FILE_CONTENT_BUCKET_THRESHOLD 2770

void loadCommitdumpFile(CommitDumpFileList *list, char *file_path) {
    FILE *f = fopen(file_path, "r+t");
    if (f == NULL) {
        return;
    }

    char *content = getContentFromFile(f);
    int content_len = strlen(content);

    char *tok = strtok(content, "\n");
    while (tok != NULL) {
        insertCommitDumpFile(list, createCommitDumpFile(tok));
        tok = strtok(NULL, "\n");
    }

    free(content);
    fclose(f);
}

char** loadDirectoryFilenames(char *directory_path) {
    struct dirent *de;
    struct stat info;
    DIR *dir = opendir(directory_path);

    if (dir != NULL) {
        de = readdir(dir);  // skip .
        de = readdir(dir);  // skip ..

        char file_path_buf[COMMITDUMP_FILES_MAX_PATH_SIZE];
        char **dir_filenames = (char **)malloc(COMMITDUMP_DIRECTORY_MAX_FILES * sizeof(char *));
        int i = 0;

        while ((de = readdir(dir)) != NULL) {
            strcpy(file_path_buf, directory_path);
            strcat(file_path_buf, "/");
            strcat(file_path_buf, de->d_name);

            stat(file_path_buf, &info);
            if (S_ISREG(info.st_mode)) {
                char *file_path = (char *)malloc(COMMITDUMP_FILES_MAX_PATH_SIZE * sizeof(char));
                strcpy(file_path, file_path_buf);

                dir_filenames[i] = file_path;
                i++;
            }
        }

        dir_filenames[i] = NULL;
        closedir(dir);
        return dir_filenames;
    } else {
        printf("ERROR: Directory '%s' not found.", directory_path);
        return NULL;
    }
}

void freeDirectoryFilenames(char **dir_filenames) {
    int i = 0;

    char *str;
    while ((str = dir_filenames[i]) != NULL) {
        free(str);
        i++;
    }

    free(dir_filenames);
}
