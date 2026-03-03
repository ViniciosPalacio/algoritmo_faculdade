palavra = input("Digite sua palavra: ").lower()
c = 0
for letra in palavra:
    if letra in "aeiouáéíóúâêôãõà":
        c += 1

print(f"A palavra '{palavra}' possui {c} vogais")