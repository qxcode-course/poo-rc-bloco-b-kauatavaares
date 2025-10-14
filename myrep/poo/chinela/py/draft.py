class Chinela:

    def __init__(self):
        self.__tamanho = 0

    def getTamanho(self) -> int:
        return self.__tamanho

    def setTamanho(self, valor: int) -> None:
        if not valor in range(20,51) or valor % 2 != 0:
            print("tamanho invalido")
            return
        else:
            self.__tamanho = valor

def main():
    chinela = Chinela()
    while chinela.getTamanho() == 0:
        print("Digite seu tamanho de chinela")
        tamanho = int(input())
        chinela.setTamanho(tamanho)
    print("parabens, você comprou um chinelo de tamanho", chinela.getTamanho())

main()
    