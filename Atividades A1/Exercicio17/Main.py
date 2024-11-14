# 17 - Implemente em Python a conversão de um AFN para um AFD para um autômato que reconhece strings terminadas em '01'.
def Main(string):
    q0, q1, q2 = 0, 1, 2
    estado_atual = q0

    for simbolo in string:
        if estado_atual == q0:
            if simbolo == '0':
                estado_atual = q1
            elif simbolo == '1':
                estado_atual = q0
        elif estado_atual == q1:
            if simbolo == '0':
                estado_atual = q1
            elif simbolo == '1':
                estado_atual = q2
        elif estado_atual == q2:
            if simbolo == '0':
                estado_atual = q1
            elif simbolo == '1':
                estado_atual = q2

    if estado_atual == q2:
        print("A string é aceita.")
    else:
        print("A string não é aceita.")

stringUser = input("Digite uma string: ")
Main(stringUser)
