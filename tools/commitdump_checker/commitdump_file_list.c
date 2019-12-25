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

CommitDumpFile* createCommitDumpFile(const char *name) {
    CommitDumpFile* file = (CommitDumpFile *)malloc(sizeof(CommitDumpFile));
    file->name = (char *)malloc((strlen(name) + 1) * sizeof(char));
    strcpy(file->name, name);
    return file;
}

void freeCommitDumpFile(CommitDumpFile *file) {
    free(file->name);
    free(file);
}

CommitDumpFileList createCommitDumpFileList() {
    CommitDumpFileList list;
    list.size = 0;

    CommitDumpFileListItem *item = (CommitDumpFileListItem *)malloc(sizeof(CommitDumpFileListItem));
    item->prox = NULL;

    list.last = item;
    list.first = list.last;

    return list;
}

void insertCommitDumpFile(CommitDumpFileList *list, CommitDumpFile *file) {
    CommitDumpFileListItem *item = (CommitDumpFileListItem *)malloc(sizeof(CommitDumpFileListItem));
    item->prox = NULL;

    list->last->file = file;
    list->last->prox = item;

    list->last = item;
    list->size++;
}

void freeCommitDumpFileList(CommitDumpFileList *list, int size) {
    int i;
    for (i = 0; i < size; i++) {
        CommitDumpFileList *item = &(list[i]);
        CommitDumpFileListItem *aux = item->first;

        item->first = item->last;
        item->size = 0;

        while (aux->prox != NULL) {
            CommitDumpFileListItem *aux2 = aux;
            aux = aux->prox;

            freeCommitDumpFile(aux2->file);
            free(aux2);
        }
        free(aux);
    }

    free(list);
}

void resetCommitDumpFileCursor(CommitDumpFileList *list) {
    list->cursor = list->first;
}

CommitDumpFile* readCommitDumpFile(CommitDumpFileList *list) {
    CommitDumpFileListItem *aux = list->cursor;
    if (aux->prox == NULL) {
        return NULL;
    }

    list->cursor = aux->prox;
    return aux->file;
}
