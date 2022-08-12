targetoutput: maincal.o libcal.so
	gcc maincal.o libcal.so -o targetoutput
libcal.so: cal.o
	gcc -shared -o libcal.so cal.o
maincal.o: maincal.c cal.h
	gcc -c maincal.c  
cal.o: cal.c
	gcc -fPIC -c cal.c
clean: 
	rm *.o targetoutput
run: 
	./targetoutput
copyheader:
	sudo cp cal.h /usr/include
copylib:
	sudo cp libcal.so /usr/lib
runldconfig:
	sudo ldconfig