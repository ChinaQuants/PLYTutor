parser: lexicalanalyzer.o
	gcc -c parser.c
	gcc -o main lexicalanalyzer.o parser.o

lexicalanalyzer.o: lexicalanalyzer.c
	gcc -c lexicalanalyzer.c
	# gcc -o lexicalanalyzer lexicalanalyzer.o

clean:
	rm -f *.o main