class Pessoa:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age

    def __str__(self):
        return f"Name {self.__name}, {self.__age}"

class Motoca:
    def __init__(self):
        self.__potencia = 1
        self.__time = 0
        self.__pessoa = None

    def inserir(self, pessoa: Pessoa) -> bool:
        if self.__pessoa is not None:
            print("fail: busy motorcycle")
            return False
        self.__pessoa = Pessoa
        return True

    def __str__(self):
       if self.__pessoa is not None:
           return f"Potencia{self.__potencia}, Time{self.__time}, Pessoa({self.__pessoa})"
       else:
           return f"Potencia{self.__potencia}, Time{self.__time}, Pessoa(vazia)"


