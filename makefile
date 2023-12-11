CC = gcc
CFLAGS = -Wall

all: programa

programa: main.c programa.c
	$(CC) $(CFLAGS) -o programa main.c programa.c

run: programa
	./programa $(ARGS)
	rm -f programa

test_c: test.c programa.c
	$(CC) $(CFLAGS) -o test_c test.c programa.c
	./test_c
	rm -f test_c

test_py: test.py
	python -m pytest test.py

