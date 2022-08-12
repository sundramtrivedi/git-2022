output: thread_create.o routin1.o routin2.o
	gcc thread_create.o routin1.o routin2.o -lpthread -o output
thread_create.o: thread_create.c
	gcc thread_create.c -c
routin1.o: routin1.c routin1.h
	gcc routin1.c -c
routin2.o: routin2.c routin2.h
	gcc routin2.c -c
clean:
	rm *.o output
run:
	./output

#make - generate object file
#make run #to run final object file (output)
#make clean - clean/remove all the .o extension and outpue file
