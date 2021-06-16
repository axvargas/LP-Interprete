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
    EOF = auto()        # ? End of file
    FUNCTION = auto()
    IDENT = auto()     # ? Identifier, name of variables
    ILLEGAL = auto()    # ? Not taking part of our language
    INT = auto()
    LBRACE = auto()
    LET = auto()        # ? Variable definitions
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    RPAREN = auto()
    SEMICOLON = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'


def lookup_token_type(literal: str) -> TokenType:
    keywords: Dict[str, TokenType] = {
        'procedimiento': TokenType.FUNCTION,
        'variable': TokenType.LET,
    }

    return keywords.get(literal, TokenType.IDENT)
