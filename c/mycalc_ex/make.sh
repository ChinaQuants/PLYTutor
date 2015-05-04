#!/bin/sh

bison --yacc -dv mycalc.y
lex mycalc.l
gcc -o mycalc y.tab.c lex.yy.c
