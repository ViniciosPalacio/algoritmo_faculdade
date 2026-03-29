def soma_digitos(n):
    if n < 10:
        return n
    return (n % 10) + soma_digitos(n // 10)

def conta_digitos(n):
    if n < 10:
        return 1
    return 1 + conta_digitos(n // 10)

def inverte_string(s):
    if len(s) <= 1:
        return s
    return s[-1] + inverte_string(s[:-1])

def eh_palindromo(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return eh_palindromo(s[1:-1])

def produto(a, b):
    if b == 0:
        return 0
    return a + produto(a, b - 1)

def maior_elemento(lista):
    if len(lista) == 1:
        return lista[0]
    max_resto = maior_elemento(lista[1:])
    return lista[0] if lista[0] > max_resto else max_resto

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def conta_ocorrencias(lista, elemento):
    if not lista:
        return 0
    soma_atual = 1 if lista[0] == elemento else 0
    return soma_atual + conta_ocorrencias(lista[1:], elemento)

def soma_lista(lista):
    if not lista:
        return 0
    return lista[0] + soma_lista(lista[1:])

def eh_primo(n, divisor=None):
    if n <= 1:
        return False
    if divisor is None:
        divisor = n - 1
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    return eh_primo(n, divisor - 1)

if __name__ == "__main__":
    print(soma_digitos(123))
    print(conta_digitos(9876))
    print(inverte_string('recursao'))
    print(eh_palindromo('arara'))
    print(produto(3, 4))
    print(maior_elemento([1, 5, 3, 9, 2]))
    print(mdc(48, 18))
    print(conta_ocorrencias([1, 2, 2, 3], 2))
    print(soma_lista([1, 2, 3, 4]))
    print(eh_primo(7))
    print(eh_primo(8))