a,b = 0,1
for n in range(1, 11):
    resultado = a + b
    a = b
    b = resultado
    print(resultado)