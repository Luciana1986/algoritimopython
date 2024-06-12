class Bichinho:
    def __init__(self, nome, fome, saude, idade):
        self.nome = nome
        self.fome = fome
        self.saude = saude
        self.idade = idade

    def mostraBichinho(self):
        print(f'nome: {self.nome}, fome: {self.fome}, saude: {self.saude}, idade: {self.idade}')

    def humor(self):
        print(f'Humor:{self.fome*self.saude}')

b = Bichinho("Tamagoshi", 5, 5, 5)
b.mostraBichinho()
b.humor()

c = Bichinho("Enog", 2, 2, 1)
c.mostraBichinho()
c.humor()