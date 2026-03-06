while True:
    try:
        n1 = float(input("Adicione a primeira nota: "))
        n2 = float(input("Adicione a segunda nota: "))
        n3 = float(input("Adicione a terceira nota: "))
    except ValueError:
        print("Apenas Nûmeros são validos!")
        continue
    media = (n1 + n2 + n3) / 3
    print(f"A sua média é: {media}")
    break