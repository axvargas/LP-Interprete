# LP-Interprete: Mattu. L(Mattu language)

## Prerequisites
python3.8 or greater

## Create virtual environment and install requirements
### Windows
```
py -m virtualenv venv
```
or
```
py -m venv venv
```
then
```
venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

### Linux
```
py -m virtualenv venv
```
or
```
py -m venv venv
```
then
```
source venv/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

## Start the RPL to test the tokens the user inputs

### Windows
```
py -m main
```

### Linux
```
python3 -m main
```

## Posible statements
```
~#@❯ variable cinco_5 = 5;
~#@❯ variable numero = 556;
~#@❯ si(5 == 5){ regresa verdadero;} si_no{ regresa falso;};
~#@❯ regresa mi_variable = verdadero

~#@❯ salir();
etc...
```

## Example
```
~#@❯ si(5 == 5){ regresa verdadero;} si_no{ regresa falso;};
```
The return in console must be the tokens found by the Mattu. L lexer
```
Type: TokenType.IF, Literal: si
Type: TokenType.LPAREN, Literal: (
Type: TokenType.INT, Literal: 5
Type: TokenType.EQ, Literal: ==
Type: TokenType.INT, Literal: 5
Type: TokenType.RPAREN, Literal: )
Type: TokenType.LBRACE, Literal: {
Type: TokenType.RETURN, Literal: regresa
Type: TokenType.TRUE, Literal: verdadero
Type: TokenType.SEMICOLON, Literal: ;
Type: TokenType.RBRACE, Literal: }
Type: TokenType.ELSE, Literal: si_no
Type: TokenType.LBRACE, Literal: {
Type: TokenType.RETURN, Literal: regresa
Type: TokenType.FALSE, Literal: falso
Type: TokenType.SEMICOLON, Literal: ;
Type: TokenType.RBRACE, Literal: }
Type: TokenType.SEMICOLON, Literal: ;
```
