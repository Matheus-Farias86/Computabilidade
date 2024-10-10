# 9 - Construa um AFD em Python que reconheça strings contendo a sequência "101".
def Main(stringUser):
    q0, q1, q2, q3 = 0, 1, 2, 3
    estado = q0

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    for symbol in stringUser:
        if estado == q0:
            if symbol == '1':
                estado = q1

        elif estado == q1:
            if symbol == '0':
                estado = q2
            elif symbol == '1':
                estado = q1
            else:
                estado = q0

        elif estado == q2:
            if symbol == '1':
                estado = q3
            else:
                estado = q0

        elif estado == q3:
            estado = q3

    if estado == q3:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)
