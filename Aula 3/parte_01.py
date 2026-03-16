import random
import time

# 1. Básico
def busca_sequencial(lista, alvo):
    """Percorre a lista sequencialmente e retorna o índice da primeira ocorrência do alvo, ou -1 se não encontrar."""
    for i, valor in enumerate(lista):
        if valor == alvo:
            return i
    return -1

# 2. Contagem de ocorrências
def contar_ocorrencias_seq(lista, alvo):
    """Conta e retorna quantas vezes o valor alvo aparece na lista."""
    contagem = 0
    for valor in lista:
        if valor == alvo:
            contagem += 1
    return contagem

# 3. Menor índice
def indice_menor_valor_seq(lista):
    """Encontra e retorna o índice do menor valor numérico presente na lista sem usar funções embutidas como min()."""
    if not lista: return -1
    menor_val = lista[0]
    menor_idx = 0
    for i in range(1, len(lista)):
        if lista[i] < menor_val:
            menor_val = lista[i]
            menor_idx = i
    return menor_idx

# 4. Busca em lista de strings
def busca_string_seq(lista, alvo):
    """Realiza busca de uma string específica em uma lista, ignorando diferenças entre maiúsculas e minúsculas (case-insensitive)."""
    alvo_lower = alvo.lower()
    for i, nome in enumerate(lista):
        if nome.lower() == alvo_lower:
            return i
    return -1

# 5. Busca com condição
def busca_maior_idade_seq(lista_dicionarios):
    """Busca em uma lista de dicionários o primeiro registro com idade igual ou superior a 18 anos e retorna seu nome."""
    for aluno in lista_dicionarios:
        if aluno.get("idade", 0) >= 18:
            return aluno.get("nome")
    return None

# 6. Busca em matriz (2D)
def busca_matriz_seq(matriz, alvo):
    """Percorre uma matriz bidimensional e retorna a tupla (linha, coluna) da primeira ocorrência do alvo."""
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == alvo:
                return (i, j)
    return (-1, -1)

# 7. Busca com limite
def busca_maior_cinquenta_seq(lista):
    """Retorna uma tupla contendo o índice e o valor do primeiro elemento estritamente maior que 50."""
    for i, valor in enumerate(lista):
        if valor > 50:
            return (i, valor)
    return (-1, -1)

# 9. Busca com múltiplos critérios
def busca_multiplos_criterios_seq(lista_tuplas):
    """Faz busca sequencial em lista de tuplas para encontrar o primeiro aluno com nota maior que 7 e nome iniciado com a letra 'A'."""
    for nome, nota in lista_tuplas:
        if nota > 7 and nome.upper().startswith('A'):
            return nome
    return "Não encontrado"