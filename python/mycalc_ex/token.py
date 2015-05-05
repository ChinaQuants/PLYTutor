# -*- coding: utf-8 -*-

from enum import IntEnum

class TokenKind(IntEnum):
    BAD_TOKEN = 0
    NUMBER_TOKEN = 1
    ADD_OPERATOR_TOKEN = 2
    SUB_OPERATOR_TOKEN = 3
    MUL_OPERATOR_TOKEN = 4
    DIV_OPERATOR_TOKEN = 5
    LEFT_PAREN_TOKEN = 6
    RIGHT_PAREN_TOKEN = 7
    END_OF_LINE_TOKEN = 8

class Token(object):

    def __init__(self):
        self.kind = TokenKind.BAD_TOKEN
        self.value = 0.0
        self.str = ''

if __name__ == '__main__':
    pass
