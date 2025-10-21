class Grafite:
    def __init__(self, calibre: float, dureza: str, tamanho: int):
        self.calibre = float(calibre)
        self.dureza = dureza
        self.size = int(tamanho)

    def usagePerSheet(self) -> int:
        gasto = {
            "HB": 1,
            "2B": 2,
            "4B": 4,
            "6B": 6
        }
        return gasto.get(self.dureza, 0)

    def __str__(self):
        return f"{self.calibre}:{self.dureza}:{self.size}"


class Lapiseira:
    def __init__(self, calibre: float = None):
        if calibre is None:
            self.calibre = None
        else:
            self.calibre = float(calibre)
        self.ponta: Grafite | None = None

    def hasGrafite(self) -> :
