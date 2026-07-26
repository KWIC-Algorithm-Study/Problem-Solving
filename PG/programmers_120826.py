#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* solution(const char* my_string, const char* letter) {
    int len = strlen(my_string);

    // 최대 원본 길이 + '\0'
    char* answer = (char*)malloc(len + 1);

    int j = 0;
    for (int i = 0; i < len; i++) {
        if (my_string[i] != letter[0]) {
            answer[j++] = my_string[i];
        }
    }

    answer[j] = '\0';

    return answer;
}
