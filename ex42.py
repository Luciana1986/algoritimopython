pessoas = []

nomes = ["Hinata", "Naruto", "Sasuke"]

sobrenomes = ["Hyuuga", "Uzumaki", "Uchiha"]

pessoas.append(nomes)

pessoas.append(sobrenomes)

lugares = []

estados = ["São Paulo", "Rio de Janeiro", "Sergipe", "Fortaleza"]

capitais = ["São Paulo", "Rio de Janeiro", "Aracaju", "Ceará"]

lugares.append(estados)

lugares.append(capitais)

conjunto = []

conjunto.append(pessoas)

conjunto.append(lugares)

print(conjunto[0][1][0])