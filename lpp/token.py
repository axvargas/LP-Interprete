from enum import (
    auto,
    Enum,
    unique
)
from typing import NamedTuple


@unique
class TokenType(Enum):
    ASSIGN = auto()
    COMMA = auto()
    EOF = auto()        # ? End of file
    FUNCTION = auto()
    INDENT = auto()     # ? Identifier, name of variables
    ILLEGAL = auto()    # ? Not taking part of our language
    INT = auto()
    LBRACE = auto()
    LET = auto()        # ? Variable definitions
    LPAREN = auto()
    PLUS = auto()
    RBRACE = auto()
    LPAREN = auto()
    SEMICOLON = auto()


class Token(NamedTuple):
    token_type: TokenType
    literal: str

    def __str__(self) -> str:
        return f'Type: {self.token_type}, Literal: {self.literal}'
