# -*- coding: utf-8 -*-

from token import Token
from token import TokenKind
from lexicalanalyzer import get_token
from lexicalanalyzer import set_line

st_look_ahead_token = Token()
st_look_ahead_token_exists = 0

def _my_get_token(token):
    global st_look_ahead_token_exists
    global st_look_ahead_token
    if st_look_ahead_token_exists:
        token.str = st_look_ahead_token.str
        token.kind = st_look_ahead_token.kind
        token.value = st_look_ahead_token.value
        st_look_ahead_token_exists = 0
    else:
        get_token(token)

def _unget_token(token):
    global st_look_ahead_token_exists
    global st_look_ahead_token
    st_look_ahead_token_exists = 1
    st_look_ahead_token = token

def _parse_primary_expression():
    token = Token()
    _my_get_token(token)
    if token.kind == TokenKind.NUMBER_TOKEN:
        return token.value
    raise ValueError('Syntax error')

def _parse_term():
    v1 = v2 = 0.0
    token = Token()

    v1 = _parse_primary_expression()

    while True:
        _my_get_token(token)
        if token.kind != TokenKind.MUL_OPERATOR_TOKEN and token.kind != TokenKind.DIV_OPERATOR_TOKEN:
            _unget_token(token)
            break

        v2 = _parse_primary_expression()
        if token.kind == TokenKind.MUL_OPERATOR_TOKEN:
            v1 *= v2
        else:
            v1 /= v2

    return v1

def parse_expression():
    v1 = v2 = 0.0
    token = Token()

    v1 = _parse_term()

    while True:
        _my_get_token(token)
        if token.kind != TokenKind.ADD_OPERATOR_TOKEN and token.kind != TokenKind.SUB_OPERATOR_TOKEN:
            _unget_token(token)
            break

        v2 = _parse_term()
        if token.kind == TokenKind.ADD_OPERATOR_TOKEN:
            v1 += v2
        else:
            v1 -= v2

    return v1

def parse_line():
    global st_look_ahead_token_exists
    st_look_ahead_token_exists = 0
    value = parse_expression()
    return value

if __name__ == '__main__':

    buf = raw_input(">>") + '\n'
    while buf:
        set_line(buf)
        value = parse_line()
        print(value)
        buf = raw_input(">>") + '\n'


