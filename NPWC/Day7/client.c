// C program for the Client Side
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/socket.h>

// inet_addr
#include <arpa/inet.h>
#include <unistd.h>

// For threading, link with lpthread
#include <pthread.h>
#include <semaphore.h>

// Function to send data to
// server socket.
void* clienthread(void* args)
{

	int client_request = *((int*)args);
	int network_socket;

	// Create a stream socket
	network_socket = socket(AF_INET,
							SOCK_STREAM, 0);

	// Initialise port number and address
	struct sockaddr_in server_address;
	server_address.sin_family = AF_INET;
	server_address.sin_addr.s_addr = INADDR_ANY;
	server_address.sin_port = htons(8989);

	// Initiate a socket connection
	int connection_status = connect(network_socket,
									(struct sockaddr*)&server_address,
									sizeof(server_address));

	// Check for connection error
	if (connection_status < 0) {
		puts("Error\n");
		return 0;
	}

	printf("Connection established\n");

	// Send data to the socket
	send(network_socket, &client_request,
		sizeof(client_request), 0);

	// Close the connection
	close(network_socket);
	pthread_exit(NULL);

	return 0;
}

// Driver Code
int main()
{
	pthread_t tid[60];
	int i = 0;
	while(1)
	{
		//accept call creates a new socket for the incoming connection
		addr_size = sizeof serverStorage;
		newSocket = accept(serverSocket, (struct sockaddr *)&serverStorage, &addr_size);
		//for each client request creates a thread and assign the client request to it to process 
		//so the main thread can entertain next request
		if(pthread_creat(&tid[i++], NULL, socketThread, &newSocket) != 0)
		{
			printf("\n Failed to create thread \n");
		}
		if(i >= 50)
		{
			i = 0;
			while(i < 50)
			{
				pthread_join(tid[i++], NULL);
			}
			i = 0;
		}
	}
	// Create connection
	// depending on the input
	
}

