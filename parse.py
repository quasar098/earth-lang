from config import *
from expression import *


def parse(lexemes: list[Token]) -> Module:
    position = 0

    def lookahead(am_fwd) -> Token:
        """Returns the lexeme infront of pos"""
        return lexemes[am_fwd+position]

    def eat(am_fwd) -> Token:
        """Mutates the lexemes"""
        food = lexemes[am_fwd + position]
        lexemes.pop(am_fwd + position)
        return food

    tree = Module(eat(0).attribute)

    return tree
