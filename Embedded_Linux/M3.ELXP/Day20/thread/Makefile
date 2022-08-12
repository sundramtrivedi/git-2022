output: thread_create.o routin1.o routin2.o 
	gcc thread_create.o routin1.o routin2.o -pthread -o output
thread_create.o: thread_create.c routin1.h routin2.h 
	gcc thread_create.c -c
routin1.o: routin1.c
	gcc routin1.c -c
routin2.o: routin2.c
	gcc routin2.c -c 
clean:
	rm *.o output
run:
	./output

#make - generate object file
#make run #to run final object file (output)
#make clean - clean/remove all the .o extension and outpue file
