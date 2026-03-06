def gerar_quadrados(limite):
    """Gera uma lista com os quadrados dos números de 1 até o limite informado"""
    quadrados = [i**2 for i in range(1, limite + 1)]
    return quadrados

def main():
    """Função principal para executar o script"""
    resultado = gerar_quadrados(10)
    print(f"Lista de quadrados de 1 a 10: {resultado}")

main()