numero = int(input("adicione um nûmero para calcular o fatorial: "))
fatorial = 1
for n in range( numero, 0, -1):
    fatorial *= n
print(f"o fatorial de {numero} é : {fatorial}")