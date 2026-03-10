def dividir(a, b):
    """Realiza a divisão e trata o erro técnico de divisão por zero"""
    try:
        resultado = a / b
        return resultado
    except ZeroDivisionError:
        return "Erro: O sistema não permite divisão por zero (divisor inválido)."

def main():
    """Executa o teste de estresse da função de divisão"""
    num1 = float(input("Digite o dividendo: "))
    num2 = float(input("Digite o divisor: "))
    
    print(f"Resultado: {dividir(num1, num2)}")
main()