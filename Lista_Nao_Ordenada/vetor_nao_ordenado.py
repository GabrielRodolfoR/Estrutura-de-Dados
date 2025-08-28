class VetorNaoOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [None] * capacidade

    def inserir(self, valor):      
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor cheio!")
        else:
            self.ultima_posicao += 1
            self.valores[self.ultima_posicao] = valor

    def imprimir(self):
            if self.ultima_posicao == -1:
                print("Vetor Vazio")
            else:
                for i in range(self.ultima_posicao + 1):
                    print(f"{i} | {self.valores[i]}")

    def pesquisar(self, valor):      
        for i in range(self.ultima_posicao + 1):
            if valor == self.valores[i]:
                return i
        return -1

    def excluir(self, valor):      
        posicao = self.pesquisar(valor)
        if posicao ==-1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores [i+1]
            self.ultima_posicao -= 1

