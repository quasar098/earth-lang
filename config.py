from tokens import *
from expression import *

COMMENT_SYMBOL = "#"
SINGLE_LEN_KEYWORDS = [
    "+",
    "-",
    "*",
    "/",
    "(",
    ")",
    "{",
    "}",
    "[",
    "]",
    "<",
    ">",
    "'",
    '"',
    "\n",
    "=",
    ",",
    ":",
    ".",
]
OTHER_KEYWORDS = [
    "print",
    "in",
    "for",
    "var",
    "int",
    "string",
    "list",
    "hashmap"
]
SPACE = " "
KEYWORDS = SINGLE_LEN_KEYWORDS + OTHER_KEYWORDS
KEYWORDS = tuple(KEYWORDS)

TYPE_KEYWORDS = [
    "hashmap",
    "int",
    "string",
    "list"
]

PATTERNS = {
    "+": AddOperator,
    "-": SubtractOperator,
    "*": MultiplyOperator,
    "/": DivideOperator,
    "(": LeftParenBrace,
    ")": RightParenBrace,
    "{": LeftCurlyBrace,
    "}": RightCurlyBrace,
    "[": LeftSquareBrace,
    "]": RightSquareBrace,
    "<": LeftAngleBrace,
    ">": RightAngleBrace,
    "'": SingleQuote,
    '"': DoubleQuote,
    "\n": Newline,
    "=": Equals,
    ",": Comma,
    ":": Colon,
    ".": Period,
}

# grammar format: [[format expected], [indexes of format which will be passed in as arguments], end result]
GRAMMAR = [
    [["var", "string", Identifier, '=', IntegerLiteral, Newline], [2, 4, 1], AssignmentExpression],
    [["var", "int", Identifier, "=", StringLiteral, Newline], [2, 4, 1], AssignmentExpression]
]
