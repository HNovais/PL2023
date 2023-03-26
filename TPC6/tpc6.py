import ply.lex as lex
import sys

tokens = [
    'INT', 'FUNCTION', 'WHILE', 'PROGRAM', 'FOR', 'IN', 'PRINT',
    'LBRACE', 'RBRACE', 'LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 
    'COMMA', 'SEMI', 'EQUALS', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE',
    'ID', 'NUM', 'COMMENT', 'DOTDOT', 'RANGLEBRACKET', 'LANGLEBRACKET'
]

t_LBRACE = r'{'
t_RBRACE = r'}'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_SEMI = r';'
t_EQUALS = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_DOTDOT = r'\.\.'
t_RANGLEBRACKET = r'\>'
t_LANGLEBRACKET = r'\<'

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z][a-zA-Z0-9]*'
    if t.value == 'int':
        t.type = 'INT'
    elif t.value == 'function':
        t.type = 'FUNCTION'
    elif t.value == 'while':
        t.type = 'WHILE'
    elif t.value == 'program':
        t.type = 'PROGRAM'
    elif t.value == 'for':
        t.type = 'FOR'
    elif t.value == 'in':
        t.type = 'IN'
    elif t.value == 'print':
        t.type = 'PRINT'
    return t

def t_NUM(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_COMMENT(t):
    r'(/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/)|(//.*)'
    pass

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t):
    print(f'Caractere ilegal: {t.value[0]}')
    t.lexer.skip(1)

lexer = lex.lex()

with open(sys.argv[1], 'r') as file:
    data = file.read()
    lexer.input(data)

    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)