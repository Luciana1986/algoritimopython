#criar no python uma classe pessoa:

class pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def mostrarpessoa(self):
        print(f'nome: {self.nome}, idade: {self.idade}, peso: {self.peso}, altura: {self.altura}')

    def envelhecer(self):
        print(f'idade: {self.idade+5}')

    def engordar(self):
        print(f'peso: {self.peso+7}')

    def emagrecer(self):
        print(f'peso: {self.peso-10}')

    def crescer(self):
        print(f'altura: {self.altura+0.2}')
        print({self.altura+0.2})

pessoa1 = pessoa("Pedro", 20, 60, 1.70)
pessoa1.mostrarpessoa()
pessoa1.envelhecer()
pessoa1.engordar()
pessoa1.emagrecer()
pessoa1.crescer()