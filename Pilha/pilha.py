class Pilha:
    def __init__(self, capacidade):
        self.topo = -1
        self.capacidade = capacidade
        self.valores = [None] * capacidade

    def pilha_cheia(self):
        return self.topo == self.capacidade - 1

    def empilhar(self, valor):
        if Pilha.pilha_cheia(self):
            print("Erro de pilha Cheia")
        else:
            self.topo += 1

        self.valores[self.topo] = valor

    def ver_topo(self):
        if self.topo != -1:
            return self.valores[self.topo]
        else:
            return -1

    def pilha_vazia(self):
        return self.topo == -1

    def desempilhar(self):
        if Pilha.pilha_vazia(self):
            print("Erro de Pilha Vazia")
        else:
            self.topo -= 1