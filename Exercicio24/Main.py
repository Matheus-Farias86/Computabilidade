# 24 - Implemente um AFD que aceite strings sobre {0, 1} onde a sequência "010" aparece pelo menos duas vezes.

def Main(stringUser):
    q0, q1, q2, q3, q4, q5, q6 = 0, 1, 2, 3, 4, 5, 6
    estado = q0

    if len(stringUser) == 0:
        print
        return

    for symbol in stringUser:
        if estado == q0:
            if symbol == '0':
                estado = q1
            else:
                estado = q0

        elif estado == q1:
            if symbol == '1':
                estado = q2
            else:
                estado = q1

        elif estado == q2:
            if symbol == '0':
                estado = q3
            else:
                estado = q0

        elif estado == q3:
            if symbol == '0':
                estado = q4
            else:
                estado = q2

        elif estado == q4:
            if symbol == '1':
                estado = q5
            else:
                estado = q1

        elif estado == q5:
            if symbol == '0':
                estado = q3
            else:
                estado = q2

    if estado == q3 or estado == q5:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)
