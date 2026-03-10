# Exercicio 1
# atividade 1
frutas = ["maçã", "banana", "laranja"]
print(frutas[1])
# atividade 2
frutas.append("uva")
frutas.remove("banana")
print(frutas)
# atividade 3
numeros = []
for i in range(1,11):
    numeros.append(i)
print(len(numeros))
# atividade 4
if 7 in numeros:
    print("SIM")
else:
    print("NÂO")
# atividade 5
print(numeros[0:3:])
# atividade 6
notas = [8.5, 7.0, 9.5, 6.0] 
notas.sort(reverse=True)
print(notas)
# atividade 7
c = 0
for i in numeros:
    if i == 5:
        c+=1
print(f"o número 5 apareceu {c} vez(s)")
# atividade 8
print(numeros[::-1])
# atividade 9
lista_nova = [i**2 for i in range(1, 9)]
print(lista_nova)
# atividade 10
palavras = ["python", "lista", "exercicio", "legal"]
palavras_2 = []
for i in palavras:
    if len(i) >= 5:
        palavras_2.append(i)
print(palavras_2)
# atividade 11
a = [1, 2, 3] 
b = [4, 5, 6]
a.extend(b)
print(a)
# atividade 12
lista=[1, 2, 2, 3, 4, 4, 5]
nova_lista = []
for c, i in enumerate(lista):
    if lista.index(i) == c:
        nova_lista.append(i)
print(nova_lista)
# atividade 13
def maior_meno(lista):
    """Essa função pega uma lista e retorna o maior e menor"""
    maior = max(lista)
    menor = min(lista)
    print(f"O maior é {maior},e o menor é {menor}")
    return maior, menor
maior_meno(lista)
# atividade 14
matriz = [[1,2,3],[4,5,6]]
print(matriz[0][1])
# atividade 15
import copy
matriz = [[1,2],[3,4]]
matriz_copia = copy.deepcopy(matriz)
matriz_copia[0][0] = 456
print(f"matriz original {matriz}\nmatrizcopia{matriz_copia}")
# atividade 16
pares = [i for i in range(0,21,2)]
print(pares)
# atividade 17
def compara_listas(lista1, lista2):
    lista1.sort()
    lista2.sort()
    return lista1 == lista2

# Testando a função
l1 = [1, 2, 3]
l2 = [3, 2, 1]
print(compara_listas(l1, l2))
# atividade 18
# Crie uma lista de 10 números aleatórios e ordene apenas os pares [cite: 19]
import random

lista_aleatoria = []
for _ in range(10):
    lista_aleatoria.append(random.randint(1, 50))

pares_ordenados = []
for i in lista_aleatoria:
    if i % 2 == 0:
        pares_ordenados.append(i)

pares_ordenados.sort()
print(f"Lista completa: {lista_aleatoria}")
print(f"Apenas os pares ordenados: {pares_ordenados}")

# atividade 19
# Remova da lista numeros os menores que 5 sem criar nova lista 
# O truque aqui é varrer a lista de trás para frente. 
# Se remover de frente para trás, os índices mudam e o loop quebra.
for i in range(len(numeros) - 1, -1, -1):
    if numeros[i] < 5:
        numeros.pop(i)
print(numeros)

# atividade 20
# Função que retorna soma acumulada [cite: 21]
def soma_acumulada(lista_num):
    nova_lista = []
    soma = 0
    for n in lista_num:
        soma += n
        nova_lista.append(soma)
    return nova_lista

print(soma_acumulada([1, 2, 3]))