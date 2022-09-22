tabela = {
    "Alface":2.50,
    "Batata":5.80,
    "Tomate":4.30,
    "Feijao":2.20,
}

print(tabela["Batata"])
print(tabela)
tabela["Alface"] = 3.50
print(tabela)
tabela["Chocolate"] = 1.50
print(tabela)

if ("Batata" in tabela): print(tabela["Batata"]) 
#maneira recomendada pois caso nao tenha vai dar erro
