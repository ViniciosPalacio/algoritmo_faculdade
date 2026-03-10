# Exercicio 2
# Ativiadade 1
aluno = { "nome": "João", "idade": 18, "nota": 9.5}
print(aluno['idade'])
# atividade 2
aluno.update(cidade = "São Paulo")
for chave in aluno:
    print(chave)
# atividade 3
for chave, valor in aluno.items():
    print(f"{chave}:{valor}")
# atividade 4
estoque = {
    "maçã": 10, "banana": 5
}
if "laranja" in estoque.keys():
    print("laranja existe")
else:
    estoque.update(laranja = 0)
print(estoque)
# Atividade 5
agenda = {
    "vinicios": {"nome": "Vinicios","telefone":22999433241, "Gmail":"vinicios@gmail.com"},
    "Karol": {"nome":"Karol","telefone":2345678, "Gmail":"Karil@gmail.com"}
}
print(agenda['vinicios']['telefone'])