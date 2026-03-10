def filtrar_pares(lista):
    """Filtra e retorna apenas os números pares de uma lista usando list comprehension"""
    pares = [i for i in lista if i % 2 == 0]
    return pares

def main():
    """Função principal para executar o filtro"""
    numeros = list(range(1, 21))  # Gerando uma lista de 1 a 20 para testar
    resultado = filtrar_pares(numeros)
    
    print(f"Lista original: {numeros}")
    print(f"Números pares filtrados: {resultado}")

main()