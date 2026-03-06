def contar_linhas(caminho):
    """Abre um arquivo de texto e retorna a quantidade total de linhas"""
    contador = 0
    with open(caminho, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            contador += 1
    return contador

def main():
    """Gerencia o fluxo de leitura e exibe o resultado"""
    try:
        arquivo_alvo = "dados.txt"
        total = contar_linhas(arquivo_alvo)
        print(f"O arquivo contém {total} linhas.")
    except FileNotFoundError:
        print("Erro: O arquivo não existe no diretório.")

main()