all:
	bison --yacc -dv mycalc.y
	lex mycalc.l
	gcc -o mycalc y.tab.c lex.yy.c

clean:
	rm -f *.c *.h mycalc *.output
