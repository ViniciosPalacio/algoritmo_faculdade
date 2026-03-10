peso = float(input("adicione seu peso em kg: "))
altura = int(input("adicione sua altura em cm: "))
imc = peso / ((altura / 100) **2 )
print(f"Seu imc é de {imc}")