#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[]) {
    if (argc < 3) {
		printf("Usage: %s <serv_ip> <serv_port>\n", argv[0]);
		exit(1);
	}

    int cfd, serv_port;
    serv_port = strtoul(argv[2], NULL, 10);

    if((cfd = socket(AF_INET, SOCK_STREAM, 0)) < 0) {
        perror("socket");
        exit(2);
    }

    struct sockaddr_in saddr = {0};
    saddr.sin_family = AF_INET;
    saddr.sin_port = htons(serv_port);
    saddr.sin_addr.s_addr = inet_addr(argv[1]);

    if (connect(cfd, (struct sockaddr *)&saddr, sizeof(saddr)) < 0) {
		perror("connect");
		close(cfd);
		exit(3);
	}

    if(send(cfd, "Hello", strlen("Hello\n"), 0) < 0) {
        perror("send");
        close(cfd);
        exit(4);
    }

    char buffer[100] = {0};

    if((recv(cfd, buffer, sizeof(buffer), 0)) < 0) {
        perror("recv");
        close(cfd);
        exit(5);
    }

    memset(buffer + 100, '\0', 1);
    printf("Data received: %s\n", buffer);

    close(cfd);
    return 0;
}