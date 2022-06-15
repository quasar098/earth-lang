from lexer import lex
from parse import parse


def main():
    with open("main.earth") as file:
        text = file.read()
    tree = parse(lex(text))
    print(tree)


if __name__ == '__main__':
    main()
