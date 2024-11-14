# 1 - Crie um autômato finito determinístico (AFD) que reconheça a linguagem sobre o alfabeto {0, 1}, onde todas as strings terminam com "1".
def Main(stringUser):

    Q0, Q1 = 0, 1
    estado = Q0

    for symbol in stringUser:
        if symbol not in '01':
            print("Entrada inválida! Use apenas 0 e 1.")
            return

        if estado == Q0:
            if symbol == '1':
                estado = Q1
            elif symbol == '0':
                estado = Q0
        elif estado == Q1:
            if symbol == '1':
                estado = Q1
            elif symbol == '0':
                estado = Q0

    if estado == Q1:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string sobre o alfabeto {0, 1}: ")

Main(stringUser)
