import os
import time
# def limpar():
#     """Esta função limpa o terminal"""
#     os.system('cls' if os.name == 'nt' else 'clear')
# # Atividade 01
# estoque = ["Notebook", "Mouse", "Teclado"]
# def adicionar_produto(estoque):
#     limpar()
#     """Esta função adiciona um produto a lista caso não já exista um
#     E recebe o lista de produtos como parâmetros"""
#     if not estoque:
#         estoque = []
#     while True:
#         while True:
#             try:
#                 produto = input("Adicione um produto: ").lower()
#                 break
#             except:
#                 print("Digite um nome valido")
#         if produto in estoque:
#             print("Produto ja existente")
#             saida = input("Precione enter para sair...")
#             return
#             break
#         else:
#             estoque.append(produto)
#             print(f"O produto '{produto}' foi adicionado")
#             saida = input("Precione enter para sair...")
#             time.sleep(1)
#             limpar()
#             return estoque
#             break
# adicionar_produto(estoque)
# #Atividade 02
# alunos = {"João": 8.5, "Maria": 9.0}
# def atualizar_nota():
#     """Essa função atualiza notas de alunos"""
#     while True:
#         while True:
#             try:
#                 nome = input("Adicone o nome do aluno: ").capitalize()
#                 nota = float(input("Adicione a nota do aluno: "))
#                 break
#             except ValueError:
#                 print("adicione um valor válido")
#                 continue
#         if nome in alunos:
#             print("Atualizando registo")
#             sair = input("precione enter para sair....")
#             alunos[nome] = nota
#             time.sleep(1)
#             limpar()
#             return alunos

#         else:
#             print("Adicionando nvos dados")
#             alunos[nome] = nota
#             sair = input("precione enter para sair....")
#             time.sleep(1)
#             limpar()
#             return alunos
# atualizar_nota()
# #Atividade 03
# def ler_quantidade():
#     """Essa função ler um imput e retorna o valor dele"""
#     while True:
#         try:
#             qtd = int(input("Adicione um número: "))
#             return qtd
#         except:
#             print("Adicione um valor inteiro valido")
#             continue
# print(ler_quantidade())
# #Atividade 04
estoque = ["Mouse", "Teclado", "Monitor", "Notebook"]
 
def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    return -1
 
print("Índice do Monitor:", busca_sequencial(estoque, "Monitor"))
print("Índice do Celular:", busca_sequencial(estoque, "Celular"))
#Atividade 05
catalogo = [101, 205, 310, 450, 520]
precos = [50.0, 120.0, 80.0, 200.0, 150.0]
 
def busca_binaria(codigos, precos, codigo):
    baixo = 0
    alto = len(codigos) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if codigos[meio] == codigo:
            return precos[meio]
        elif codigos[meio] < codigo:
            baixo = meio + 1
        else:
            alto = meio - 1
    return "Produto não encontrado"
 
print("Preço do código 310:", busca_binaria(catalogo, precos, 310))