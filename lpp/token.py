from enum import (
    auto,
    Enum,
    unique
)
from typing import (
    NamedTuple,
    Dict
)


@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    DIVISION = auto()
    ELSE = auto()
    EOF = auto()        # ? End of file
    EQ = auto()
    FALSE = auto()
    FUNCTION = auto()
    GT = auto()
    G_EQ_T = auto()
    IDENT = auto()     # ? Identifier, name of variables
    IF = auto()
    ILLEGAL = auto()    # ? Not taking part of our language
    INT = auto()
    LBRACE = auto()
    LET = auto()        # ? Variable definitions
    LT = auto()
    L_EQ_T = auto()
    NEGATION = auto()
    NOT_EQ = auto()
    MINUS = auto()
    MULTIPLICATION = auto()
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RETURN = auto()
    RPAREN = auto()
    SEMICOLON = auto()
    TRUE = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'


def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'falso': TokenType.FALSE,
        'procedimiento': TokenType.FUNCTION,
        'regresa': TokenType.RETURN,
        'si': TokenType.IF,
        'si_no': TokenType.ELSE,
        'variable': TokenType.LET,
        'verdadero': TokenType.TRUE
    }

    return keywords.get(literal, TokenType.IDENT)
