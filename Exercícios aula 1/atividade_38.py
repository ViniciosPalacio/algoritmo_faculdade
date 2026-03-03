def salvar_dados(nome_arquivo, conteudo):
    """Cria um arquivo de texto e escreve a string informada dentro dele"""
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        arquivo.write(conteudo)

def main():
    """Define o conteúdo e executa o processo de escrita"""
    nome = "saida.txt"
    texto = "Este é o log gerado pelo sistema.\nOperação finalizada com sucesso."
    
    salvar_dados(nome, texto)
    print(f"Dados gravados com sucesso no arquivo '{nome}'.")

main()