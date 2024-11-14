# 18 - Desenvolva um AFD que reconheça a linguagem de strings sobre {0, 1} com número ímpar de '0's e '1's.
def Main(stringUser):
    contador_zeros = 0
    contador_uns = 0

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    for symbol in stringUser:
        if symbol == '0':
            contador_zeros += 1
        elif symbol == '1':
            contador_uns += 1
        else:
            print("Entrada inválida! Use apenas 0 e 1.")
            return

    if contador_zeros % 2 == 1 and contador_uns % 2 == 1:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)
