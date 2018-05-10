test-mymath: test-mymath.o libmymath.a
	gcc -o test-mymath test-mymath.o libmymath.a
test-mymath.o: test-mymath.c
	gcc -c test-mymath.c
libmymath.a: libmymath.o
	ar crv libmymath.a libmymath.o
libmymath.o: libmymath.c
	gcc -c libmymath.c
