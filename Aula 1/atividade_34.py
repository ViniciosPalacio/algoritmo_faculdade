def calcular_fatorial(numero):
    """Calcula o fatorial de um número usando recursão (sem usar for ou while)"""
    if numero == 0 or numero == 1:
        return 1
    return numero * calcular_fatorial(numero - 1)

numero_digitado = int(input("Digite um número inteiro: "))

resultado = calcular_fatorial(numero_digitado)

print(f"O fatorial de {numero_digitado} é {resultado}")