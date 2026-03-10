def achar_primo(numero):
    """recebe um número inteiro e valida se é primo ou não"""
    teste = 0
    for i in range(numero, 0, -1):
        if numero % i == 0:
            teste+=1
    if teste == 2:
        return "é um número primo"
    else:
        return "não é um número primo"
numero = int(input("adicione um número inteiro: "))
resultado = achar_primo(numero)
print(resultado)