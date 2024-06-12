class Clienteconta:
    def __init__(self,nome,numero,saldo,telefone,limite):
        self.nome = str(nome)
        self.numero = str(nome)
        self.saldo = float(saldo)
        self.telefone = str(telefone)
        self.limite = float(limite)
        self.extrato = []

    def saque(self, valor):
      if valor < (self.saldo + self.limite):
          self.saldo -= valor
          self.extrato.append("- saque: " + str(valor))
          return valor
      else:
          print ('saldo insuficiente')

    def deposito(self, valor):
        self.saldo += valor
        self.extrato.append("+ deposito:" + str(valor))

    def extrato(self):
        print ('------Extrat0------')
        print('conta:', self.numero+'\n')
        for i in self.extrato:
            print( i + '\n')
        print('saldo:', self.saldo)
        print('limite:', self.limite)
        print('disponivel:', self.saldo+self.limite)

    def mostraCliente(self):
        print(f'nome: {self.nome}, telefone: {self.telefone}, Numero: {self.numero}, Saldo: {self.saldo}, limite: {self.limite}')

teste = Clienteconta('Ana', '90999-0000', '10029', '100.00', '3000.00')
teste.mostraCliente()
teste.saque(50)
teste.mostraCliente()
teste.deposito(200)
teste.mostraCliente()
