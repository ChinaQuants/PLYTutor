# -*- coding: utf-8 -*-

from token import Token
from token import TokenKind
from enum import IntEnum

st_line = ''
st_line_pos = 0

class LexerStatus(IntEnum):
    INITIAL_STATUS = 0
    IN_INT_PART_STATUS = 1
    DOT_STATUS = 2
    IN_FRAC_PART_STATUS = 3

def get_token(token):
    global st_line
    global st_line_pos

    out_pos = 0
    status = LexerStatus.INITIAL_STATUS
    token.kind = TokenKind.BAD_TOKEN

    while st_line_pos < len(st_line):
        current_char = st_line[st_line_pos]
        if (status == LexerStatus.IN_INT_PART_STATUS or status == LexerStatus.IN_FRAC_PART_STATUS) \
            and not current_char.isdigit() and current_char != '.':
            token.kind = TokenKind.NUMBER_TOKEN
            token.value = float(token.str)
            return

        if current_char.isspace():
            if current_char == '\n':
                token.kind = TokenKind.END_OF_LINE_TOKEN
                return
            st_line_pos += 1
            continue

        if out_pos >= len(token.str):
            token.str += st_line[st_line_pos]
        else:
            tmp = list(token.str)
            tmp[out_pos] = st_line[st_line_pos]
            token.str = ''.join(tmp[:out_pos+1])

        st_line_pos += 1
        out_pos += 1

        if current_char == '+':
            token.kind = TokenKind.ADD_OPERATOR_TOKEN
            return
        elif current_char == '-':
            token.kind = TokenKind.SUB_OPERATOR_TOKEN
            return
        elif current_char == '*':
            token.kind = TokenKind.MUL_OPERATOR_TOKEN
            return
        elif current_char == '/':
            token.kind = TokenKind.DIV_OPERATOR_TOKEN
            return
        elif current_char.isdigit():
            if status == LexerStatus.INITIAL_STATUS:
                status = LexerStatus.IN_INT_PART_STATUS
            elif status == LexerStatus.DOT_STATUS:
                status = LexerStatus.IN_FRAC_PART_STATUS
        elif current_char == '.':
            if status == LexerStatus.IN_INT_PART_STATUS:
                status = LexerStatus.DOT_STATUS
            else:
                raise ValueError('syntax error.')
        else:
            raise ValueError('bad character(%s)' % current_char)


def set_line(line):
    global st_line
    global st_line_pos
    st_line = line
    st_line_pos = 0

if __name__ == '__main__':

    def parse_line(buf):
        token = Token()
        set_line(buf)

        while True:
            get_token(token)
            if token.kind == TokenKind.END_OF_LINE_TOKEN:
                break
            else:
                print("kind..%d, str..%s" % (token.kind, token.str))

    buf = raw_input(">>") + '\n'
    while buf:
        parse_line(buf)
        buf = raw_input(">>") + '\n'
