# 5 - Implemente em Python um AFD que aceite qualquer string binária que comece e termine com o mesmo caractere.
def Main(stringUser):
    q0, q1, q2, q3, q_reject = 0, 1, 2, 3, 4
    estado = q0

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    first_char = stringUser[0]

    for i, symbol in enumerate(stringUser):
        if symbol not in '01':
            print("Entrada inválida! Use apenas 0 e 1.")
            return

        if estado == q0:
            if symbol == '0':
                estado = q1
            elif symbol == '1':
                estado = q2

        elif estado == q1:
            if i == len(stringUser) - 1:
                if symbol == first_char:
                    estado = q3
                else:
                    estado = q_reject

        elif estado == q2:
            if i == len(stringUser) - 1:
                if symbol == first_char:
                    estado = q3
                else:
                    estado = q_reject

    if estado == q3:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string binária: ")
Main(stringUser)
