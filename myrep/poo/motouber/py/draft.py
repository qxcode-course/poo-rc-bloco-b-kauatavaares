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

    def receber(self, valor: int):
        self.__dinheiro += valor

    def __str__(self):
        if self.__dinheiro.is_integer():
            return f"{self.__nome}:{int(self.__dinheiro)}"
        else:
            return f"{self.__nome}:{self.__dinheiro}"
class Moto:
        def __init__(self):
            self.__custo = 0
            self.__passa: Pessoa | None = None
            self.__motorista: Pessoa | None = None

        def setDrive(self, pessoas:Pessoa):
            self.__motorista = pessoas
        def subirMotorista(self, pessoa: Pessoa):
            if self.__motorista is not None:
                print("fail: no driver")
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
            if self.__motorista is None:
                print("fail: no driver")
                return
            self.__passa = pessoa
            self.__custo = 0

        def descerPass(self):
            if self.__passa is None:
                print("fail: nao tem passa")
                return

            pago = self.__custo


            if self.__motorista is not None:
                self.__motorista.receber(pago)

            print(f"{self.__passa.getNome()}:{pago:} left")
            self.__passa = None
            self.__custo = 0

        def dirigir(self, km: float):
            if self.__passa is None:
                print("fail: nao ha passageiro para dirigir")
                return
            self.__custo += km * 1

        def leavePassageiro(self):
            if self.__passa is None:
                print("fail: não tem passageiro")
                return

            pagamento = self.__custo
            pago = self.__passa.pagar(pagamento)

            if pago < pagamento:
                print("fail: Passenger does not have enough money")

            if self.__motorista is not None:
                self.__motorista.receber(pagamento)

            print(f"{self.__passa.getNome()}:{int(self.__passa.getDinheiro())} left")
            self.__passa = None
            self.__custo = 0

        def __str__(self):
            motorista = str(self.__motorista) if self.__motorista else "None"
            passa = str(self.__passa) if self.__passa else "None"
            return f"Cost: {int(self.__custo)}, Driver: {motorista}, Passenger: {passa}"

        def getMotorista(self):
            pass


def main():
    moto = Moto()
    pessoas = {}

    while True:
        line =  input()
        print("$" + line)
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "setDriver":
            nome = args[1]
            dinheiro = float(args[2])
            if nome not in pessoas:
                pessoas[nome] = Pessoa(nome, dinheiro)
            moto.subirMotorista(pessoas[nome])
        elif args[0] == "setPass":
            nome = args[1]
            dinheiro = float(args[2])
            if nome not in pessoas:
                pessoas[nome] = Pessoa(nome, dinheiro)
            moto.subirPass(pessoas[nome])
        elif args[0] == "drive":
            km = float(args[1])
            moto.dirigir(km)
        elif args[0] == "leavePass":
            moto.leavePassageiro()
        elif args[0] == "show":

            print(moto)
main()