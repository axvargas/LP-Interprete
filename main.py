from lpp.repl import start_repl


def main() -> None:
    print('''
        
    ███╗░░░███╗░█████╗░████████╗████████╗██╗░░░██╗░░░  ██╗░░░░░
    ████╗░████║██╔══██╗╚══██╔══╝╚══██╔══╝██║░░░██║░░░  ██║░░░░░
    ██╔████╔██║███████║░░░██║░░░░░░██║░░░██║░░░██║░░░  ██║░░░░░
    ██║╚██╔╝██║██╔══██║░░░██║░░░░░░██║░░░██║░░░██║░░░  ██║░░░░░
    ██║░╚═╝░██║██║░░██║░░░██║░░░░░░██║░░░╚██████╔╝██╗  ███████╗
    ╚═╝░░░░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░░╚═════╝░╚═╝  ╚══════╝

Bienvenido a MATTU. L v.0.1 REPL el lenguaje de programación en español


Esta es la version 0.1 del REPL(Read Evaluate Print Loop) del lenguaje
de programación MATTU. L, aquí puedes escribir sentencias del lenguaje
y el REPL las descompondrá en los distintos Tokens que el Lexer del 
lenguaje encuentre en tu sentencia

    -Sentencias
        salir();            -> Sale del REPL
        
        variable num = 5;   -> Sentencia de asignación
        
        si(n == 2){
            regresa 1;
        } sino{
            regresa 0;
        };                  -> Sentencia de if else

        etc...
Escribe una sentencia del lenguaje para empezar
    ''')

    start_repl()


if __name__ == '__main__':
    main()
