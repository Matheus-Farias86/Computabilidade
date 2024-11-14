# 13 - Desenvolva um AFD que reconheça strings binárias onde o número de '1's seja maior que o número de '0's.
def Main(stringUser):
    q0, q1, q2 = 0, 1, 2
    estado = q0
    numZeros = 0
    numUns = 0

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    for symbol in stringUser:
        if symbol not in '01':
            print("Entrada inválida! Use apenas '0' e '1'.")
            return

        if estado == q0:
            if symbol == '0':
                numZeros += 1
                estado = q2
            elif symbol == '1':
                numUns += 1
                estado = q1

        elif estado == q1:
            if symbol == '0':
                numZeros += 1
                estado = q1
            elif symbol == '1':
                numUns += 1
                estado = q1

        elif estado == q2:
            if symbol == '0':
                numZeros += 1
                estado = q2
            elif symbol == '1':
                numUns += 1
                estado = q1

    if numUns > numZeros:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string binária: ")
Main(stringUser)
