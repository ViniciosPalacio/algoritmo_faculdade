def adicionar_tarefas(tarefas):
    nome = input("Adicione a nova tarefa: ")
    tarefas.append({"nome": nome, "feito": False})
    print("Tarefa adicionada com sucesso.")
    return tarefas

def listar_tarefas(tarefas):
    if not tarefas:
        print("Não existem tarefas registradas.")
        return
    for i, t in enumerate(tarefas):
        status = "FEITO" if t["feito"] else "ESPERA"
        print(f"{i + 1}. {t['nome']} - {status}")
def validar_tarefa(tarefas):
    if not tarefas:
        print("Não existem tarefas para validar.")
        return tarefas
        
    listar_tarefas(tarefas) 
    
    while True:
        try:
            escolha = int(input("Escolha o número da tarefa para concluir: "))
            if 1 <= escolha <= len(tarefas):
                break
            else:
                print("Alvo inválido. Escolha um número da lista.")
        except ValueError:               
            print("Entrada negada. Use apenas números inteiros.")
            
    indice_real = escolha - 1

    if tarefas[indice_real]["feito"] == True:
        print("Desperdício de energia. Esta tarefa já está FEITA.")
    else:
        tarefas[indice_real]["feito"] = True
        print("Tarefa atualizada para FEITO.")
        
    return tarefas

def remover_tarefas(tarefas):
    if not tarefas:
        print("Sem tarefas para remover.")
        return tarefas
        
    listar_tarefas(tarefas)
    
    while True:
        try:
            escolha = int(input("Escolha o número da tarefa para remover: "))
            if 1 <= escolha <= len(tarefas):
                break
            else:
                print("Alvo inválido. Escolha um número da lista.")
        except ValueError:               
            print("Entrada negada. Use apenas números inteiros.")
            
    indice_real = escolha - 1
    tarefa_removida = tarefas.pop(indice_real)
    print(f"Tarefa '{tarefa_removida['nome']}' eliminada do sistema.")
    return tarefas

def main():
    tarefas = [] 
    
    while True:
        print("\n--- BASE DE OPERAÇÕES ---")
        print("1. Adicionar tarefa")
        print("2. Listar todas as tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("5. Sair")
        
        try:
            escolha = int(input("Escolha uma das opções: "))
        except ValueError:
            print("Falha: Digite um número de 1 a 5.")
            continue
            
        if escolha == 1:
            tarefas = adicionar_tarefas(tarefas)
        elif escolha == 2:
            listar_tarefas(tarefas)
        elif escolha == 3:
            tarefas = validar_tarefa(tarefas)
        elif escolha == 4:
            tarefas = remover_tarefas(tarefas)
        elif escolha == 5:
            print("Extração concluída. Encerrando sistema...")
            break
        else:
            print("Opção fora do radar.")

main()