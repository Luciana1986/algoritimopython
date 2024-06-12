class Carro:
    def __init__(self, marca, modelo, placa, nrodas):
        self.marca = str(marca)
        self.modelo = str(modelo)
        self.placa = str(placa)
        self.nrodas = (nrodas)

    def mostraCarro(self):
        print(f'marca:{self.marca}, Modelo: {self.modelo}, Placa: {self.placa}, Nrodas{self.nrodas}')


teste = Carro('vw', 'Gol', 'RJA98-0999', 4)
teste.mostraCarro()
teste = Carro('Ford', 'fusion', 'RJB98-098', 8)
teste.mostraCarro()
