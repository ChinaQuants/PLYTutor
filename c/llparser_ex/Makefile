CC = gcc
CFLAGS = -O2

parser: lexicalanalyzer.o
	$(CC) -c $(CFLAGS) parser.c
	$(CC) -o main lexicalanalyzer.o parser.o

lexicalanalyzer.o: lexicalanalyzer.c
	$(CC) -c $(CFLAGS) lexicalanalyzer.c
	# $(CC) -o lexicalanalyzer lexicalanalyzer.o

clean:
	rm -f *.o main
