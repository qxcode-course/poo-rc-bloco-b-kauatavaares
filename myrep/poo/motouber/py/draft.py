class Pessoa:
    def __init__(self, nome: str, dinheiro: float):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome
    def getDinheiro(self):
        return self.__dinheiro



class Moto:
        def __init__(self,custo: int, passa: Pessoa, motorista: int):
            self.__custo = custo
            self.__passa = passa
            self.__motorista = motorista

        def pagar(self):
