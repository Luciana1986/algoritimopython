class Cachorro:
    def __init__(self, nome, cor, altura, peso):
        self.nome = str(nome)
        self.cor = str(cor)
        self.altura = str(altura)
        self.peso = (peso)

    def mostracachorro(self):
        print(f'nome:{self.nome}, cor: {self.cor}, altura: {self.altura}, peso {self.peso}')

    def latir(self):
        print("Au au!")

cachorro1 = Cachorro('Rex', 'branco', '50cm', '4')
cachorro1.mostracachorro()

cachorro1.latir()  # Saída: Au au!

cachorro2 = Cachorro('jack', 'bege', '50cm', '6')
cachorro2.mostracachorro()

cachorro2.latir()