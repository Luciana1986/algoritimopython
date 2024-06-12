class Contacorrente:
    def __init__(self, numeroconta:int, nome:str, saldo:float):
        self.numeroconta = int(numeroconta)
        self.nome = str(nome)
        self.saldo = float(saldo)

    def alterarnome(self, nome):
        self.nome = str(nome)

    def deposito(self, saldo):
        self.saldo += float(saldo)

    def saque(self, saldo):
        self.saldo -= float(saldo)

    def mostraconta(self):
        print(f'numeroconta: {self.numeroconta}, nome: {self.nome}, saldo: {self.saldo}')

conta1 = Contacorrente('000134', 'Ana', '400')
conta1.mostraconta()
conta1.alterarnome('Ana Silva')
conta1.mostraconta()
conta1.deposito(200)
conta1.mostraconta()