def analisador(numero):
    if numero == 2:
        return True
    if numero == 3:
        return True
    if numero == 5:
        return True
    if numero == 7:
        return True
    elif numero <= 0:
        return False
    elif numero % 3 == 0:
        return False
    elif numero % 5 == 0:
        return False
    elif numero % 7 == 0:
        return False
    elif numero % 2 == 0:
        return False
    else:
        return True


def menu():
    while True:
        op = input("Deseja continuar :\n [1]Sim\n [2]Não\n")
        if op == "1":
            return True
        elif op == "2":
            return False


def entrada():
    while True:
        try:
            print("------------------------\n")
            numero = int(input("Digite o numero inteiro que deseja verificar se é primo ou não: "))
            return numero
        except:
            print("Ensira um numero inteiro!")


op = True
while op:
    numero = entrada()
    if analisador(numero):
        print("o numero ", numero, " é primo")
    else:
        print("o numero ", numero, " não é primo")
    op = menu()