class Pessoa:
    def __init__(self, nome: str, dinheiro: float):
        self.__nome = nome
        self.__dinheiro = dinheiro

    def getNome(self):
        return self.__nome

    def getDinheiro(self):
        return self.__dinheiro

    def pagar(self, valor: float):
        if valor <= self.__dinheiro:
            self.__dinheiro -= valor
            return valor
        else:
            pago = self.__dinheiro
            self.__dinheiro = 0
            return pago

    def receber(self, valor: float):
        self.__dinheiro += valor

    def __str__(self):
        return f"{self.__nome}: {self.__dinheiro}"

class Moto:
        def __init__(self):
            self.__custo = 0
            self.__passa: Pessoa | None = None
            self.__motorista: Pessoa | None = None

        def subirMotorista(self, pessoa: Pessoa):
            if self.__motorista is not None:
                print("fail: tem motorista")
                return
            self.__motorista = pessoa

        def descerMotorista(self):
            if self.__motorista is None:
                print("fail: nao tem motorista")
                return
            self.__motorista = None

        def subirPass(self, pessoa: Pessoa):
            if self.__passa is not None:
                print("fail: tem passageiro")
                return
            elif self.__passa is None:
                print("fail: nao tem passageiro")
                return
            self.__passa = pessoa
            self.__custo = 0

        def descerPass(self):
            if self.__passa is None:
                print("fail: nao tem passa")
                return

            pago = self.__passa.pagar(self.__custo)

            if self.__motorista is not None:
                self.__motorista.receber(self.__custo)

            print(f"{self.__passa.getNome()} pagou r${pago:.2f}")
            self.__passa = None
            self.__custo = 0.0

        def dirigir(self, km: float):
            if self.__passa is None:
                print("fail: nao ha passageiro para dirigir")
                return
            self.__custo += km * 1

        def __str__(self):

