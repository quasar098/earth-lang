from typing import Any


class Token:
    attribute: Any

    def __repr__(self):
        return f"<Token({self.__dict__})>"


class Newline(Token):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return "<Newline>"


class Identifier(Token):
    def __init__(self, name: str):
        self.attribute = name

    def __repr__(self):
        return f"<Identifier({self.attribute})>"


class Operator(Token):
    def __repr__(self):
        return f"<Operator>"


class AddOperator(Operator):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<Add>"


class SubtractOperator(Operator):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<Subtract>"


class MultiplyOperator(Operator):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<Multiply>"


class DivideOperator(Operator):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<Divide>"


class Literal(Token):
    def __repr__(self):
        return f"<Literal>"


class Keyword(Token):
    def __init__(self, name: str):
        self.attribute = name

    def __repr__(self):
        return f"<Keyword({self.attribute})>"

    def __eq__(self, other: "Keyword"):
        return self.attribute == other.attribute


class StringLiteral(str, Literal):
    def __init__(self, value: str):
        super().__init__()
        self.attribute = value

    def __str__(self):
        return f"<String({self.attribute})>"

    def __repr__(self):
        return f"<String({self.attribute})>"


class IntegerLiteral(Literal, int):
    def __init__(self, integer: int):
        super().__init__()
        self.attribute = integer

    def __repr__(self):
        return f"<Int({self.attribute})>"


class Brace(Token):
    def __repr__(self):
        return f"<Brace>"


class LeftParenBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<LeftParen>"


class RightParenBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<RightParen>"


class LeftSquareBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<LeftSquare>"


class RightSquareBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<RightSquare>"


class LeftCurlyBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<LeftCurly>"


class RightCurlyBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<RightCurly>"


class LeftAngleBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return "<LeftAngle>"


class RightAngleBrace(Brace):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return "<RightAngle>"


class Quote(Token):
    pass


class SingleQuote(Quote):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<SingleQuote>"


class DoubleQuote(Quote):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<DoubleQuote>"


class Equals(Token):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return "<Equals>"


class Comma(Token):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return "<Comma>"


class Colon(Token):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return "<Colon>"


class Period(Token):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return "<Period>"


class Title(Token):
    def __init__(self, attr=None):
        self.attribute = attr

    def __repr__(self):
        return f"<Title({self.attribute})>"
