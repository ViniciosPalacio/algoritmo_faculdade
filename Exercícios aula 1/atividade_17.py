n = int(input("adicione quantos termos deseja somar: "))
soma = 0
for i in range(1,n + 1):
    soma += i
print(f"A soma de 1 até {n} é: {soma}")