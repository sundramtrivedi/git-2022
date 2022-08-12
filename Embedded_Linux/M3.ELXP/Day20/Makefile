output: man.o sum.o mul.o
	gcc man.o sum.o mul.o -o output
man.o: man.c sum.h mul.h
	gcc man.c -c
sum.o: sum.c
	gcc sum.c -c
mul.o: mul.c	
	gcc mul.c -c
clean:
	rm *.o output
run:
	./output

#make - generate object file
#make run #to run final object file (output)
#make clean - clean/remove all the .o extension and outpue file
