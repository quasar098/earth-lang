from config import *
from expression import *


def parse(lexemes: list[Token]):
    position = 0

    def lookahead(amount):
        return lexemes[amount+position]
    tree = Planet()

    while position != len(lexemes):
        lexeme = lexemes[position]
        position += 1
        ast.append(lexeme)

    return ast

