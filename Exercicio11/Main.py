# 11 - Construa um AFD para uma linguagem sobre o alfabeto {a, b}, que reconheça strings com um número ímpar de 'a's.
def Main(stringUser):
    q_par, q_impar, q_reject = 0, 1, 2
    estado = q_par

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    for symbol in stringUser:
        if symbol not in 'ab':
            print("Entrada inválida! Use apenas 'a' e 'b'.")
            return

        if estado == q_par:
            if symbol == 'a':
                estado = q_impar
            elif symbol == 'b':
                estado = q_par

        elif estado == q_impar:
            if symbol == 'a':
                estado = q_par
            elif symbol == 'b':
                estado = q_impar

    if estado == q_impar:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string sobre o alfabeto {a, b}: ")
Main(stringUser)
