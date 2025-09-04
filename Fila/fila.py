class Fila:
    def __init__(self, capacidade):
        self.final = -1
        self.inicio = 0
        self.elementos = 0
        self.capacidade = capacidade
        self.valores = [None] * capacidade

    def fila_cheia(self):
        return self.elementos == self.capacidade

    def enfileirar(self, valor):
        if Fila.fila_cheia(self):
            print("Erro de fila Cheia")
            return

        if self.final == self.capacidade - 1:
            self.final = -1

        self.final += 1
        self.valores[self.final] = valor
        self.elementos += 1

    def fila_vazia(self):
        return self.elementos == 0

    def desenfileirar(self):
        if Fila.fila_vazia(self):
            print("Erro de Fila Vazia")
            return

        temp = self.valores[self.inicio]
        self.inicio += 1

        if self.inicio == self.capacidade:
            self.inicio = 0

        self.elementos -= 1
        return temp

    def primeiro(self):
        if Fila.fila_vazia(self):
            return -1
        return self.valores[self.inicio]
