#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

pthread_mutex_t mutex;

void *routine(void* cf) {
    int cfd = *(int *)cf;
    char buffer[100] = {0};
    recv(cfd, buffer, 2000, 0);

    printf("%s\n", buffer);
    
    send(cfd, buffer, 100, 0);

    pthread_mutex_lock(&mutex);
    printf("%ld\n", pthread_self());
    pthread_mutex_unlock(&mutex);

    char buffer2[20];
    long int id = pthread_self();
    sprintf(buffer2, "%ld", id);
    send(cfd, buffer2, 100, 0);
}

int main(int argc, char* argv[]) {
    int sfd, cfd, port_no;
    struct sockaddr_in saddr = {0};

    port_no = 10007;

    sfd = socket(PF_INET, SOCK_STREAM, 0);

    saddr.sin_family = AF_INET;
    saddr.sin_port = htons(port_no);
    saddr.sin_addr.s_addr = inet_addr("127.0.0.1");

    bind(sfd, (struct sockaddr *)&saddr, sizeof(saddr));

    if(listen(sfd, 5) == 0) {
        printf("Listening\n");
    }
    else {
        printf("ERROR");
    }

    pthread_t t1[5];

    for(int i = 0; i < 5; i++){
        struct sockaddr_storage caddr = {0};
        socklen_t len = sizeof(caddr);
        cfd = accept(sfd, (struct sockaddr *)&caddr, &len);

        if(pthread_create(&t1[i], NULL, routine, &cfd)!= 0 ) {
            printf("Failed to create thread\n");
        }

        if(i > 5) {
            i = 0;
            while(i < 5)
                pthread_join(t1[i],NULL);
            i = 0;
        }
        close(cfd);
    }
    close(sfd);
    return 0;
}