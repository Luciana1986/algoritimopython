class Estado:
    def __init__(self, nome, sigla):
        self.nome = nome
        self.sigla = sigla

    def adicionar_cidade(self, cidade):
    self.cidades.append(cidade)

    def populacao(self):
        return sum([cidade.populacao for cidade in self.cidades])

class Cidade:
    def __init__(self, nome, populacao):
        self.nome = nome
        self.populacao = populacao
        self.estado = None

    def __str__(self):
        return f"Cidade (nome={self.nome}, populacao={self.populacao}, estado={self.estado}")

am = Estado("Amazonas", "AM")
am.adiciona_cidade(Cidade("Manaus", 180))
am.adiciona_cidade(Cidade("PariLins", 80))
am.adiciona_cidade(Cidade("IlacoaLiara", 60))
sp = Estado(" São Paulo", "SP")
sp.adiciona_cidade(Cidade("São Paulo", 500))
sp.adiciona_cidade(Cidade("Guarulhos", 200))
rj = Estado(" Rio de Janeiro", "RJ")
rj.adiciona_cidade(Cidade("Rio de Janeiro", 400))
rj.adiciona_cidade(Cidade("São Gonçalo", 200))
rj.adiciona_cidade(Cidade("Duque de caxias", 100))

for estado in [am, sp, rj]:
    print(f"Estado: {estado.nome}, Sigla: {estado.sigla}")
    for cidade in estado.cidades:
        print(f"Cidade: {cidade.nome} populacao: {cidade.populacao}")
        print(f"População de Estado: {estado.populacao()}\n")