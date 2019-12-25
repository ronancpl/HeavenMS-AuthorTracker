#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

// string hash version by chqrlie - https://stackoverflow.com/questions/20462826/hash-function-for-strings-in-c
unsigned int strhash(const char *word) {
    unsigned int hash = 0, c;

    size_t i = 0;
    for (i = 0; word[i] != '\0'; i++) {
        c = (unsigned char)word[i];
        hash = (hash << 3) + (hash >> (sizeof(hash) * CHAR_BIT - 3)) + c;
    }
    return hash % UINT_MAX;
}

char *getContentFromFile(FILE *f) {
    char *content = (char *)malloc(1073741825 * sizeof(char));  // 1MB
    content[0] = 0;

    char str[1024];
    while (fgets(str, sizeof(str), f)) {
        strcat(content, str);
    }

    return content;
}
