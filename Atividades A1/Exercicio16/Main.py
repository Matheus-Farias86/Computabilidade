# 16 - Construa um AFD para reconhecer strings sobre {0, 1} onde os '0's aparecem em blocos consecutivos.
def Main(stringUser):
    q0, q1, q2, q_reject = 0, 1, 2, 3
    estado = q0

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    for symbol in stringUser:
        if estado == q0:
            if symbol == '0':
                estado = q1
            elif symbol == '1':
                estado = q2

        elif estado == q1:
            if symbol == '0':
                estado = q1
            elif symbol == '1':
                estado = q2

        elif estado == q2:
            if symbol == '0':
                estado = q_reject
            elif symbol == '1':
                estado = q2

    if estado == q1 or estado == q2:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)
