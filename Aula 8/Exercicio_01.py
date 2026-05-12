import os
import time
import random

def limpar():
    """Limpa o terminal de forma limpa e multiplataforma."""
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_matriz(matriz):
    """Renderiza a matriz atualizada na tela."""
    for linha in matriz:
        print("  ".join(linha))
    print()

def exercicio_caca_tesouro():
    """Lógica principal do Exercício 1."""
    limpar()
    print("----- MÓDULO 1: CAÇA AO TESOURO -----")
    
    tamanho = 5
    matriz = [["~" for _ in range(tamanho)] for _ in range(tamanho)]
    
    linha_tesouro = random.randint(0, tamanho - 1)
    coluna_tesouro = random.randint(0, tamanho - 1)
    
    tentativas = 0
    encontrado = False
    
    while not encontrado:
        exibir_matriz(matriz)
        print(f"Tentativas contabilizadas: {tentativas}")
        
        try:
            linha_jogada = int(input("Informe a linha (0 a 4): "))
            coluna_jogada = int(input("Informe a coluna (0 a 4): "))
            
            # Validação de limites da matriz
            if linha_jogada < 0 or linha_jogada >= tamanho or coluna_jogada < 0 or coluna_jogada >= tamanho:
                print("Aviso: Coordenadas fora do mapa. Tente novamente.")
                time.sleep(1.5)
                limpar()
                continue
                
            tentativas += 1
            
            if linha_jogada == linha_tesouro and coluna_jogada == coluna_tesouro:
                encontrado = True
                matriz[linha_jogada][coluna_jogada] = "X"
                limpar()
                exibir_matriz(matriz)
                print(f"Sucesso! Tesouro localizado em {tentativas} tentativas.")
                input("\nPressione Enter para retornar ao menu principal...")
            else:
                # Cálculo de distância (diferença máxima entre as coordenadas)
                dist_linha = abs(linha_jogada - linha_tesouro)
                dist_coluna = abs(coluna_jogada - coluna_tesouro)
                distancia = max(dist_linha, dist_coluna)
                
                # Marca a jogada errada no mapa
                matriz[linha_jogada][coluna_jogada] = "O"
                
                print("\nStatus da Busca:")
                if distancia == 1:
                    print("Dica: Muito perto!")
                elif distancia == 2 or distancia == 3:
                    print("Dica: Perto!")
                else:
                    print("Dica: Longe!")
                
                time.sleep(1.5)
                limpar()
                
        except ValueError:
            print("Erro de tipo. Informe apenas números inteiros.")
            time.sleep(1.5)
            limpar()

def exercicio_cavalo():
    """Lógica principal do Exercício 2."""
    limpar()
    print("----- MÓDULO 2: SIMULADOR DE XADREZ (CAVALO) -----")
    
    tamanho = 8
    matriz = [["-" for _ in range(tamanho)] for _ in range(tamanho)]
    
    try:
        linha_inicial = int(input("Posição inicial - Linha (0 a 7): "))
        coluna_inicial = int(input("Posição inicial - Coluna (0 a 7): "))
        
        if linha_inicial < 0 or linha_inicial >= tamanho or coluna_inicial < 0 or coluna_inicial >= tamanho:
            print("Aviso: A posição inicial deve estar dentro do tabuleiro (0 a 7).")
            time.sleep(2)
            return
            
        matriz[linha_inicial][coluna_inicial] = "C"
        
        # Vetores de movimento possíveis em "L"
        movimentos = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]
        
        for mov_l, mov_c in movimentos:
            nova_linha = linha_inicial + mov_l
            nova_coluna = coluna_inicial + mov_c
            
            # Blindagem: O cavalo não pode sair da matriz
            if 0 <= nova_linha < tamanho and 0 <= nova_coluna < tamanho:
                matriz[nova_linha][nova_coluna] = "*"
        
        limpar()
        print(f"Análise concluída para o Cavalo em ({linha_inicial}, {coluna_inicial}):")
        print("Legenda: 'C' = Origem | '*' = Movimentos Válidos | '-' = Vazio\n")
        exibir_matriz(matriz)
        
        input("\nPressione Enter para retornar ao menu principal...")
        
    except ValueError:
        print("Erro de tipo. Informe apenas números inteiros.")
        time.sleep(1.5)

def main():
    while True:
        limpar()
        print("----- AMBIENTE DE DESENVOLVIMENTO: MATRIZES -----")
        print("1. Executar Módulo: Caça ao Tesouro")
        print("2. Executar Módulo: Algoritmo do Cavalo")
        print("3. Encerrar Sessão")
        
        escolha = input("\nInsira a diretriz (1-3): ")
        
        if escolha == '1':
            exercicio_caca_tesouro()
        elif escolha == '2':
            exercicio_cavalo()
        elif escolha == '3':
            print("Encerrando o ambiente...")
            time.sleep(1)
            break
        else:
            print("Diretriz não reconhecida no sistema.")
            time.sleep(1)

if __name__ == '__main__':
    main()