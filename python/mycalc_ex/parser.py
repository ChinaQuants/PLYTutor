# -*- coding: utf-8 -*-

from token import Token
from token import TokenKind
from lexicalanalyzer import get_token
from lexicalanalyzer import set_line
from lexicalanalyzer import LineHolder

class LookAheadHolder(object):

    def __init__(self):
        self.st_look_ahead_token = Token()
        self.st_look_ahead_token_exists = 0

def _my_get_token(token, line_holder, look_ahead_holder):
    if look_ahead_holder.st_look_ahead_token_exists:
        token.str = look_ahead_holder.st_look_ahead_token.str
        token.kind = look_ahead_holder.st_look_ahead_token.kind
        token.value = look_ahead_holder.st_look_ahead_token.value
        look_ahead_holder.st_look_ahead_token_exists = 0
    else:
        get_token(token, line_holder)

def _unget_token(token, look_ahead_holder):
    look_ahead_holder.st_look_ahead_token_exists = 1
    look_ahead_holder.st_look_ahead_token = token

def _parse_primary_expression(line_holder, look_ahead_holder):
    token = Token()
    _my_get_token(token, line_holder, look_ahead_holder)
    minus_flag = False
    value = 0.0

    if token.kind == TokenKind.SUB_OPERATOR_TOKEN:
        minus_flag = True
    else:
        _unget_token(token, look_ahead_holder)

    _my_get_token(token, line_holder, look_ahead_holder)

    if token.kind == TokenKind.NUMBER_TOKEN:
        return token.value
    elif token.kind == TokenKind.LEFT_PAREN_TOKEN:
        value = parse_expression(line_holder, look_ahead_holder)
        _my_get_token(token, line_holder, look_ahead_holder)
        if token.kind != TokenKind.RIGHT_PAREN_TOKEN:
            raise ValueError('Syntax error')
    else:
        _unget_token(token, look_ahead_holder)

    if minus_flag:
        value = -value

    return value

def _parse_term(line_holder, look_ahead_holder):
    v1 = v2 = 0.0
    token = Token()

    v1 = _parse_primary_expression(line_holder, look_ahead_holder)

    while True:
        _my_get_token(token, line_holder, look_ahead_holder)
        if token.kind != TokenKind.MUL_OPERATOR_TOKEN and token.kind != TokenKind.DIV_OPERATOR_TOKEN:
            _unget_token(token, look_ahead_holder)
            break

        v2 = _parse_primary_expression(line_holder, look_ahead_holder)
        if token.kind == TokenKind.MUL_OPERATOR_TOKEN:
            v1 *= v2
        else:
            v1 /= v2

    return v1

def parse_expression(line_holder, look_ahead_holder):
    v1 = v2 = 0.0
    token = Token()

    v1 = _parse_term(line_holder, look_ahead_holder)

    while True:
        _my_get_token(token, line_holder, look_ahead_holder)
        if token.kind != TokenKind.ADD_OPERATOR_TOKEN and token.kind != TokenKind.SUB_OPERATOR_TOKEN:
            _unget_token(token, look_ahead_holder)
            break

        v2 = _parse_term(line_holder, look_ahead_holder)
        if token.kind == TokenKind.ADD_OPERATOR_TOKEN:
            v1 += v2
        else:
            v1 -= v2

    return v1

def parse_line(line_holder, look_ahead_holder):
    look_ahead_holder.st_look_ahead_token_exists = 0
    value = parse_expression(line_holder, look_ahead_holder)
    return value

if __name__ == '__main__':

    line_holder = LineHolder()
    look_ahead_holder = LookAheadHolder()

    buf = raw_input(">>") + '\n'
    while buf:
        set_line(buf, line_holder)
        value = parse_line(line_holder, look_ahead_holder)
        print(value)
        buf = raw_input(">>") + '\n'


