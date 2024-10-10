# 22 - Desenvolva um AFD que reconheça uma linguagem onde a diferença entre o número de 'a's e 'b's seja múltipla de 3.

def Main(stringUser):
    q0, q1, q2 = 0, 1, 2
    estado = q0
    contadorA, contadorB = 0, 0

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    for symbol in stringUser:
        if symbol == 'a':
            contadorA += 1
        elif symbol == 'b':
            contadorB += 1

        diferenca = contadorA - contadorB

        if diferenca % 3 == 0:
            estado = q0
        elif diferenca % 3 == 1:
            estado = q1
        elif diferenca % 3 == 2:
            estado = q2

    if estado == q0:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)
