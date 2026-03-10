import math
def area_circulo(raio):
    """Essa função calcula a área do circulo"""
    area = math.pi * (raio ** 2)
    return area
def main():
    raio = float(input("adicione o valor do raio: "))
    resultado = area_circulo(raio)
    print(f"A área desse circulo é de {resultado: .2f}")
main()