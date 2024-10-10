# 4 - Desenvolva um AFD que aceite strings com pelo menos um '0'.
def Main(stringUser):
    Q0, Q1 = 0, 1
    estado = Q0

    for symbol in stringUser:

        if estado == Q0:
            if symbol == '0':
                estado = Q1

    if estado == Q1:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)