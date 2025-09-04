class VetorOrdenado:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.ultima_posicao = -1
        self.valores = [None] * capacidade

    # Insira um novo valor
    def inserir(self, valor):
        if self.ultima_posicao == self.capacidade - 1:
            print("Vetor cheio!")
            return

        else:
            posicao = 0
            for i in range(self.ultima_posicao + 1):
                if self.valores[i] > valor:
                    break

                elif i == self.ultima_posicao:
                    posicao = i + 1

            x = self.ultima_posicao

            while x >= posicao:  # Organiza o novo valor na posição correta
                self.valores[x + 1] = self.valores[x]
                x -= 1
            self.valores[posicao] = valor
            self.ultima_posicao += 1

    # Mostra o Vetor em Ordem
    def imprimir(self):
        if self.ultima_posicao == -1:
            print("Vetor Vazio")
        else:
            for i in range(self.ultima_posicao + 1):
                print(f"{i} | {self.valores[i]}")

    # Procura a posição do valor
    def pesquisa_linear(self, valor):
        for i in range(self.ultima_posicao + 1):
            if self.valores[i] > valor or i == self.ultima_posicao:
                return -1

            elif self.valores[i] == valor:
                return i

    def pesquisa_binaria(self, valor):
        limite_inferior = 0
        limite_superior = self.ultima_posicao

        while True:
            posicao_atual = (limite_inferior + limite_superior) / 2

            if self.valores[posicao_atual]:
                return posicao_atual
            elif limite_inferior > limite_superior:
                return -1
            else:
                if self.valores[posicao_atual] < valor:
                    limite_inferior = posicao_atual + 1
                else:
                    limite_inferior = posicao_atual - 1

    def excluir(self, valor):
        posicao = self.pesquisar(valor)
        if posicao == -1:
            return -1
        else:
            for i in range(posicao, self.ultima_posicao):
                self.valores[i] = self.valores[i + 1]
            self.ultima_posicao -= 1
