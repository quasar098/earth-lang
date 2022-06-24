from config import *


def gen_lexemes(text: str):
    out = []
    lexeme = ""
    commenting = False
    in_string = ""
    comment_eater = ""
    title = "Unnamed Module"
    string_cooldown = False
    for index, char in enumerate(text):  # loop over each char in the source text

        # in string handling
        if char in "\"'":
            if not string_cooldown:
                string_cooldown = True
                in_string = char
                out.append(char)
                continue
            else:
                string_cooldown = False
        if len(in_string) > 0:
            lexeme += char
            if text[index + 1] == in_string:
                in_string = ""
                out.append(lexeme)
                lexeme = ""
            continue

        # comment handling
        if char == COMMENT_SYMBOL:
            commenting = True  # start a comment
        if commenting:
            comment_eater += char
            if char == "\n":  # break out of a comment if newline
                commenting = False
                if comment_eater[:2] == "##":
                    title = comment_eater[2:-1].lstrip()
                comment_eater = ""
            continue

        # add lexemes
        if char != SPACE:  # if it is not a space, add it to lexeme builder
            lexeme += char
        if lexeme in SINGLE_LEN_KEYWORDS or (lexeme in OTHER_KEYWORDS and text[index + 1] == SPACE) \
                or text[index + 1] in KEYWORDS or text[index + 1] == SPACE:  # idk what this does
            if lexeme != '':  # only add if lexeme has something
                out.append(lexeme)
            lexeme = ""
    out.insert(0, title)
    return out


def lex(text: str) -> list[Token]:
    out = []
    lexemes = gen_lexemes(text)
    title, lexemes = lexemes[0], lexemes[1:]
    in_string = None
    for lexeme in lexemes:
        if lexeme in PATTERNS:
            out.append(PATTERNS[lexeme]())
            if lexeme in "'\"":  # handle quotes to string
                if in_string is None:
                    in_string = lexeme
                else:
                    in_string = None
        elif lexeme in OTHER_KEYWORDS:
            out.append(Keyword(lexeme))
        else:
            if lexeme.isnumeric():
                out.append(IntegerLiteral(int(lexeme)))
            elif in_string is not None:
                out.append(StringLiteral(lexeme))
            else:
                out.append(Identifier(lexeme))

    # compress newlines
    compressed = []
    last_was_newline = True
    for token in out:
        if isinstance(token, Newline):
            if last_was_newline:
                continue
            else:
                last_was_newline = True
        else:
            last_was_newline = False
        compressed.append(token)
    compressed.insert(0, Title(title))
    return compressed
