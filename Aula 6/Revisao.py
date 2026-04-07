# =============================================
# Exercício 1 - Estoque de Produtos
# =============================================
estoque1 = ["Notebook", "Mouse", "Teclado"]

def adicionar_produto(lista, produto):
    if produto not in lista:
        lista.append(produto)
    print("Estoque atual:", lista)

# BUG CORRIGIDO: Ordem dos parâmetros invertida (Lista primeiro, Produto depois)
adicionar_produto(estoque1, "Monitor")
adicionar_produto(estoque1, "Mouse")

# =============================================
# Exercício 2 - Cadastro de Alunos
# =============================================
alunos2 = {"João": 8.5, "Maria": 9.0}

def atualizar_nota(nome, nota):
    # Dicionários em Python já criam a chave se não existir ou atualizam se existir
    alunos2[nome] = nota
    print(f"Nota de {nome} atualizada para {nota}")

atualizar_nota("Pedro", 7.5)
print(alunos2)


# =============================================
# Exercício 3 - Validação de Entrada com try/except
# =============================================
def ler_quantidade():
    # BUG CORRIGIDO: Adicionado laço while para repetir até receber entrada válida
    while True:
        try:
            qtd = int(input("Quantidade: "))
            return qtd
        except ValueError:
            print("Erro! Digite apenas números inteiros.")

print("Quantidade válida:", ler_quantidade())


# =============================================
# Exercício 4 - Busca Sequencial
# =============================================
estoque4 = ["Mouse", "Teclado", "Monitor", "Notebook"]

def busca_sequencial(lista, item):
    for i in range(len(lista)):
        if lista[i] == item:
            return i
    # BUG CORRIGIDO: Retornar -1 em vez de None conforme o enunciado
    return -1

print("Índice do Monitor:", busca_sequencial(estoque4, "Monitor"))
print("Índice do Celular:", busca_sequencial(estoque4, "Celular"))


# =============================================
# Exercício 5 - Busca Binária
# =============================================
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


# =============================================
# Exercício 6 - Inventário com Dicionário
# =============================================
inventario = {
    "Notebook": {"qtd": 10, "preco": 2500},
    "Mouse": {"qtd": 50, "preco": 80}
}

def consultar_produto(nome):
    if nome in inventario:
        dados = inventario.get(nome)
        print(f"{nome} - Estoque: {dados['qtd']} | Preço: R${dados['preco']}")
    else:
        print("Produto não encontrado")

consultar_produto("Mouse")
consultar_produto("Headset")


# =============================================
# Exercício 7 - Busca Sequencial com try/except
# =============================================
alunos7 = [
    {"matricula": 1001, "nome": "Ana"},
    {"matricula": 1002, "nome": "Bruno"}
]

def buscar_por_matricula(mat):
    try:
        mat = int(mat)
    except ValueError:
        return "Erro: A matrícula deve ser um número!"

    for aluno in alunos7:
        if aluno["matricula"] == mat:
            return aluno["nome"]
    return "Aluno não encontrado"

print(buscar_por_matricula("1001"))
print(buscar_por_matricula("abc"))


# =============================================
# Exercício 8 - Busca Binária com Ordenação
# =============================================
vendas = [150, 80, 220, 90, 300]

def busca_binaria_vendas(lista, valor):
    # BUG CORRIGIDO: Usar sorted() para não alterar a lista original do escopo global
    lista_ordenada = sorted(lista)
    baixo, alto = 0, len(lista_ordenada) - 1
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if lista_ordenada[meio] == valor:
            return meio
        elif lista_ordenada[meio] < valor:
            baixo = meio + 1
        else:
            alto = meio - 1
    return -1

print("Índice do valor 220 na lista ordenada:", busca_binaria_vendas(vendas, 220))


# =============================================
# Exercício 9 - Relatório de Vendas com Dicionário
# =============================================
vendas_dia = {"Notebook": "2500", "Mouse": 80, "Teclado": "150"}

def total_vendas(vendas):
    total = 0
    for valor in vendas.values():
        try:
            total += float(valor)
        # BUG CORRIGIDO: Substituído o 'except:' genérico por ValueError/TypeError
        except (ValueError, TypeError):
            pass
    return total

print("Total de vendas:", total_vendas(vendas_dia))


# =============================================
# Exercício 10 - Estudo de Caso: Controle de Estoque
# =============================================
estoque_tech = [
    {"nome": "Notebook Dell", "quantidade": 8, "preco": 2899.90},
    {"nome": "Mouse Logitech", "quantidade": 45, "preco": 89.90},
    {"nome": "Teclado Mecânico", "quantidade": 12, "preco": 249.90},
    {"nome": "Monitor 24''", "quantidade": 15, "preco": 899.90}
]

def cadastrar_produto():
    nome = input("Nome do produto: ")
    try:
        quantidade = int(input("Quantidade inicial: "))
        preco = float(input("Preço unitário: "))
    except ValueError:
        print("Erro: quantidade e preço devem ser números!")
        return
    estoque_tech.append({"nome": nome, "quantidade": quantidade, "preco": preco})
    print(f"Produto {nome} cadastrado com sucesso!")

def buscar_produto(nome_busca):
    for produto in estoque_tech:
        if produto["nome"].lower() == nome_busca.lower():
            return produto
    return None

def atualizar_quantidade(nome, quantidade_alterada):
    produto = buscar_produto(nome)
    if produto:
        nova_quantidade = produto["quantidade"] + quantidade_alterada
        # BUG CORRIGIDO: Trava de segurança para impedir estoque negativo
        if nova_quantidade < 0:
            print(f"Erro: Operação cancelada. Não há estoque suficiente (Atual: {produto['quantidade']}).")
        else:
            produto["quantidade"] = nova_quantidade
            print(f"Estoque atualizado! {produto['nome']} agora tem {produto['quantidade']} unidades.")
    else:
        print("Produto não encontrado!")

def produto_mais_barato_acima_de(preco_minimo):
    precos = sorted([p["preco"] for p in estoque_tech])
    baixo = 0
    alto = len(precos) - 1
    resultado = None
    while baixo <= alto:
        meio = (baixo + alto) // 2
        if precos[meio] >= preco_minimo:
            resultado = precos[meio]
            alto = meio - 1  # Continua buscando à esquerda para achar o menor valor válido
        else:
            baixo = meio + 1
    
    if resultado is None:
        return "Nenhum produto encontrado acima desse preço."
    
    # Busca o nome do produto correspondente a esse preço
    for p in estoque_tech:
        if p["preco"] == resultado:
            return f"Produto mais barato acima de R${preco_minimo}: {p['nome']} (R${resultado:.2f})"

def gerar_relatorio():
    if not estoque_tech:
        print("Estoque vazio!")
        return
    total_estoque = 0
    print("\n--- Relatório de Estoque ---")
    for produto in estoque_tech:
        valor_total = produto["quantidade"] * produto["preco"]
        total_estoque += valor_total
        print(f"{produto['nome']:25} | Qtd: {produto['quantidade']:3} | Preço: R${produto['preco']:8.2f} | Total: R${valor_total:8.2f}")
    print(f"\nValor total em estoque: R${total_estoque:.2f}")

def menu():
    while True:
        print("\n=== TechZone - Controle de Estoque ===")
        print("1. Cadastrar novo produto")
        print("2. Buscar produto")
        print("3. Atualizar quantidade")
        print("4. Produto mais barato acima de um preço")
        print("5. Gerar relatório completo")
        print("6. Sair")

        try:
            opcao = int(input("\nEscolha uma opção: "))
        except ValueError:
            print("Opção inválida! Digite um número inteiro.")
            continue

        if opcao == 1:
            cadastrar_produto()
        elif opcao == 2:
            nome = input("Digite o nome do produto: ")
            prod = buscar_produto(nome)
            if prod:
                print(f"Encontrado: {prod['nome']} - Qtd: {prod['quantidade']} - R${prod['preco']:.2f}")
            else:
                print("Produto não encontrado.")
        elif opcao == 3:
            nome = input("Nome do produto: ")
            try:
                qtd = int(input("Quantidade a adicionar/subtrair (use negativo para saída): "))
                atualizar_quantidade(nome, qtd)
            except ValueError:
                print("Quantidade inválida! Deve ser um número inteiro.")
        elif opcao == 4:
            try:
                preco = float(input("Preço mínimo: R$"))
                print(produto_mais_barato_acima_de(preco))
            except ValueError:
                print("Preço inválido! Deve ser um número.")
        elif opcao == 5:
            gerar_relatorio()
        elif opcao == 6:
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    menu()