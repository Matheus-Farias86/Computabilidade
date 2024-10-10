# 3 - Construa um AFD que reconheça a linguagem de strings que contenham exatamente dois '1's sobre o alfabeto {0, 1}.
def Main(stringUser):
    Q0, Q1, Q2 = 0, 1, 2
    estado = Q0

    for symbol in stringUser:
        if symbol not in '01':
            print("Entrada inválida! Use apenas 0 e 1.")
            return

        if estado == Q0:
            if symbol == '1':
                estado = Q1

        elif estado == Q1:
            if symbol == '1':
                estado = Q2

        elif estado == Q2:
            if symbol == '1':
                print("A string não é aceita.")
                return

    if estado == Q2:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string sobre o alfabeto {0, 1}: ")
Main(stringUser)
