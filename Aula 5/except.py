def exercicio_1():
    try:
        n1 = float(input())
        n2 = float(input())
        print(n1 / n2)
    except ValueError:
        print("Valor inválido")
    except ZeroDivisionError:
        print("Divisão por zero")

def exercicio_2():
    cores = {'vermelho': (255, 0, 0), 'verde': (0, 255, 0), 'azul': (0, 0, 255)}
    try:
        cor = input().lower()
        print(cores[cor])
    except KeyError:
        print("Cor não encontrada")

def exercicio_3():
    try:
        numero = float(input())
        if numero > 10:
            print("Número válido")
    except ValueError:
        print("Valor inválido")
    else:
        print("Programa executado com sucesso")
    finally:
        print("Programa encerrado")

class SenhaInvalidaError(Exception):
    pass

def exercicio_4(senha):
    try:
        if len(senha) < 8 or not any(c.isdigit() for c in senha):
            raise SenhaInvalidaError("Senha inválida: mínimo 8 caracteres e 1 número")
        print("Senha aceite")
    except SenhaInvalidaError as e:
        print(e)

def exercicio_5():
    try:
        saldo = float(input())
        valor = float(input())
        if valor > saldo:
            raise ValueError("Saldo insuficiente")
        saldo -= valor
        print(f"Sucesso. Saldo atual: {saldo}")
    except ValueError as e:
        print(e)