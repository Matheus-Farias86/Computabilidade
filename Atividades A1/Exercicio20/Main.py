# 20 - Implemente um AFD para strings sobre {a, b} onde a sequência 'ab' aparece exatamente uma vez.
def Main(stringUser):
    q0, q1, q2, q3 = 0, 1, 2, 3
    estado = q0

    if len(stringUser) == 0:
        print("A string não é aceita.")
        return

    for symbol in stringUser:
        if estado == q0:
            if symbol == 'a':
                estado = q1
            elif symbol == 'b':
                estado = q0

        elif estado == q1:
            if symbol == 'b':
                estado = q2
            elif symbol == 'a':
                estado = q1

        elif estado == q2:
            if symbol == 'a':
                estado = q3
            elif symbol == 'b':
                estado = q3

        elif estado == q3:
            print("A string não é aceita.")
            return

    if estado == q2:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)
