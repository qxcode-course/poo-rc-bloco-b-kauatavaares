class Camisa:
    def __init__(self):
        self.__tamanho: str = ""

    def getTamanho(self) -> str:
        return self.__tamanho

    def setTamanho(self, valor: str):
        tam_valido = ["PP", "P", "M", "G", "GG", "XG"]

        if valor in tam_valido:
            self.__tamanho = valor
        else:
            print(f"Erro: tamanho inválido")

def main():
    camisa = Camisa()

    while camisa.getTamanho() == "":
        tamanho = input()
        camisa.setTamanho(tamanho)

    print(f"Parabens! Você comprou uma camisa tamanho {camisa.getTamanho()}.")

main()