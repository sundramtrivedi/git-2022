#include <stdio.h>
#include <pthread.h>

void toDisplay(FILE* fd) {
    char buffer[100];
    fread(buffer, 10, 1, fd);
    printf("%s\n", buffer);
}

void * hello(void *fd) {
    toDisplay(fd);
    pthread_exit(NULL);
}

int main(void) {
    FILE *fd = fopen("try.txt", "r");
    toDisplay(fd);
    rewind(fd);
    pthread_t tid;
    pthread_create(&tid, NULL, hello, fd);
    pthread_join(tid, NULL);
    return 0;
}