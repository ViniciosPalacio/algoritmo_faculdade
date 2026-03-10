def somar(x,y):
    """Essa função recebe dois números e os soma"""
    soma = x + y
    return soma
primeiro_numero = float(input("digite o primeiro número: "))
segundo_número = float(input("digite o segundo número: "))
resultado = somar(primeiro_numero,segundo_número)
print(f"a soma de {primeiro_numero} e {segundo_número} é {resultado}")
