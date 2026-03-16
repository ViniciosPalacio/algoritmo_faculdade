# 1. Básico
def busca_binaria(lista, alvo):
    """Executa o algoritmo de busca binária em uma lista ordenada para encontrar o índice do alvo em tempo O(log n)."""
    esq, dir = 0, len(lista) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return -1

# 2. Menor índice (primeira ocorrência)
def busca_binaria_primeira_ocorrencia(lista, alvo):
    """Em uma lista ordenada com duplicatas, encontra e retorna o menor índice (primeira ocorrência) do valor alvo."""
    esq, dir = 0, len(lista) - 1
    resultado = -1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            resultado = meio
            dir = meio - 1 
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return resultado

# 3. Maior índice (última ocorrência)
def busca_binaria_ultima_ocorrencia(lista, alvo):
    """Em uma lista ordenada com duplicatas, encontra e retorna o maior índice (última ocorrência) do valor alvo."""
    esq, dir = 0, len(lista) - 1
    resultado = -1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            resultado = meio
            esq = meio + 1 
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return resultado

# 4. Busca de inserção
def busca_binaria_insercao(lista, alvo):
    """Retorna o índice exato onde o alvo deveria ser inserido para que a lista continue ordenada."""
    esq, dir = 0, len(lista) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
    return esq 

# 5. Busca em lista de strings ordenada
def busca_binaria_strings(lista, alvo):
    """Realiza busca binária em uma lista de strings ordenada alfabeticamente, ignorando maiúsculas e minúsculas."""
    esq, dir = 0, len(lista) - 1
    alvo_lower = alvo.lower()
    while esq <= dir:
        meio = (esq + dir) // 2
        meio_lower = lista[meio].lower()
        if meio_lower == alvo_lower:
            return meio
        elif meio_lower < alvo_lower:
            esq = meio + 1
        else:
            dir = meio - 1
    return -1

# 6. Encontrar o valor mais próximo
def busca_binaria_mais_proximo(lista, alvo):
    """Caso o alvo não exista, encontra e retorna o índice do valor numérico mais próximo a ele na lista ordenada."""
    if not lista: return -1
    esq, dir = 0, len(lista) - 1
    if alvo <= lista[esq]: return 0
    if alvo >= lista[dir]: return dir
    
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo:
            return meio
        elif lista[meio] < alvo:
            esq = meio + 1
        else:
            dir = meio - 1
            
    if (lista[esq] - alvo) < (alvo - lista[dir]):
        return esq
    return dir

# 7. Contar elementos menores que X
def contar_menores_binaria(lista, alvo):
    """Usa a lógica de busca binária para descobrir quantos elementos na lista ordenada são estritamente menores que o alvo."""
    return busca_binaria_insercao(lista, alvo) 

# 8. Busca em matriz ordenada
def busca_matriz_ordenada(matriz, alvo):
    """Busca otimizada em uma matriz bidimensional onde as linhas e colunas já estão ordenadas. Retorna a tupla (linha, coluna)."""
    if not matriz or not matriz[0]: return (-1, -1)
    linhas, colunas = len(matriz), len(matriz[0])
    l, c = 0, colunas - 1
    while l < linhas and c >= 0:
        if matriz[l][c] == alvo:
            return (l, c)
        elif matriz[l][c] > alvo:
            c -= 1
        else:
            l += 1
    return (-1, -1)

# 9. Desafio - Rotated Sorted Array
def busca_binaria_rotacionada(lista, alvo):
    """Executa busca binária modificada em uma lista que foi rotacionada em um pivô desconhecido, sem ordenar a lista previamente."""
    esq, dir = 0, len(lista) - 1
    while esq <= dir:
        meio = (esq + dir) // 2
        if lista[meio] == alvo: return meio
        
        if lista[esq] <= lista[meio]: 
            if lista[esq] <= alvo < lista[meio]:
                dir = meio - 1
            else:
                esq = meio + 1
        else: 
            if lista[meio] < alvo <= lista[dir]:
                esq = meio + 1
            else:
                dir = meio - 1
    return -1