from no import No


class ListaEncadeadaSimples:
    def __init__(self):
        self.primeiro = None

    def inserir_inicio(self, valor):
        atual = No(valor)
        atual.proximo = self.primeiro
        self.primeiro = atual

    def mostrar(self):
        if self.primeiro is None:
            print("Lista vazia")
            return

        atual = self.primeiro
        while atual is not None:
            atual.mostra_no()
            atual = atual.proximo

    def excluir_inicio(self):
        if self.primeiro is None:
            print("Erro: lista vazia")
            return None

        temp = self.primeiro
        self.primeiro = self.primeiro.proximo
        temp.proximo = None
        return temp

    def pesquisar(self, valor):
        if self.primeiro is None:
            print("Erro: lista vazia")
            return None

        atual = self.primeiro
        while atual is not None:
            if atual.valor == valor:
                return atual
            atual = atual.proximo

        return None

    def excluir_qualquer(self, valor):
        if self.primeiro is None:
            print("Erro: lista vazia")
            return None

        atual = self.primeiro
        anterior = None

        while atual is not None:
            if atual.valor == valor:
                if anterior is None:
                    self.primeiro = atual.proximo
                else:
                    anterior.proximo = atual.proximo

                atual.proximo = None
                return atual

            anterior = atual
            atual = atual.proximo

        return None
