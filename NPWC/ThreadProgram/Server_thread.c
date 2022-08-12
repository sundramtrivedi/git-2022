#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

pthread_mutex_t mutex;

void *routine(void* cf) {
    pthread_mutex_lock(&mutex);
    int cfd = *(int *)cf;
    char buffer[50] = {0};
    int ret = 0;
    if((ret = recv(cfd, buffer, sizeof(buffer), 0)) < 0) {
        perror("recv");
        close(cfd);
        exit(6);
    }

    printf("%s\n", buffer);

    if(send(cfd, buffer, 100, 0) < 0) {
        perror("send");
        exit(7);
    }

    printf("%ld\n", pthread_self());
    char buffer2[20];
    long int id = pthread_self();
    sprintf(buffer2, "%ld", id);

    if(send(cfd, buffer2, 20, 0) < 0) {
        perror("send");
        close(cfd);
        exit(7);
    }
    pthread_mutex_unlock(&mutex);
}

int main(int argc, char* argv[]) {
    pthread_t t1[5];

    if (argc < 2)
	{
		printf("Usage: %s <port_no>\n", argv[0]);
		exit(1);
	}

    int sfd, cfd, port_no;
    port_no = strtoul(argv[1], NULL, 10);

    if((sfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket");
        exit(2);
    }

    struct sockaddr_in saddr = {0};
    saddr.sin_family = AF_INET;
    saddr.sin_port = htons(port_no);
    saddr.sin_addr.s_addr = INADDR_ANY;

    if(bind(sfd, (struct sockaddr *)&saddr, sizeof(saddr)) < 0) {
        perror("bind");
        close(sfd);
        exit(3);
    }

    if(listen(sfd, 5) < 0) {
        perror("listen");
        close(sfd);
        exit(4);
    }
    
    for(int i = 0; i < 5; i++){
        struct sockaddr_in caddr = {0};
        socklen_t len = sizeof(caddr);
        if((cfd = accept(sfd, (struct sockaddr *)&caddr, &len)) < 0) {
            perror("accept");
            exit(5);
        }

        if(pthread_create(&t1[i], NULL, routine, &cfd) != 0) {
            printf("ERROR in creating thread\n");
        }

        if(i > 5) {
            i = 0;
            while(1 < 5) {
                pthread_join(t1[i], NULL);
            }
            i = 0;
        }
        
        close(cfd);
    }
    close(sfd);
    return 0;
}