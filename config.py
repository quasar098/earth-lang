from tokens import *

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
