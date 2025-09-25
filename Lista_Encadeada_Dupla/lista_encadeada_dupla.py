from no import No


class ListaEncadeadaDupla:
    def __init__(self):
        self.primeiro = None
        self.ultimo = None

    def lista_vazia(self):
        return self.primeiro == None

    # Inserir
    def inserir_inicio(self, valor):
        novo = No(valor)

        if ListaEncadeadaDupla.lista_vazia(self):
            self.ultimo = novo
        else:
            self.primeiro.anterior = novo

        novo.proximo = self.primeiro
        self.primeiro = novo

    def inserir_final(self, valor):
        novo = No(valor)

        if ListaEncadeadaDupla.lista_vazia(self):
            self.primeiro = novo

        else:
            self.ultimo.proximo = novo
            novo.anterior = self.ultimo

        self.ultimo = novo

    # Excluir
    def excluir_inicio(self):
        temp = self.primeiro

        if self.primeiro.proximo == None:
            self.ultimo = None

        else:
            self.primeiro.proximo.anterior = None

        proximo = self.primeiro.proximo
        return temp

    def excluir_final(self):
        temp = self.ultimo

        if self.primeiro.proximo == None:
            self.primeiro = None

        else:
            self.ultimo.anterior.proximo = None

        self.ultimo = self.ultimo.anterior

        return temp
    
    def excluir_qualquer(self, valor):
        atual = self.primeiro
        
        while atual.valor != valor:
            atual = atual.proximo
            
            if atual == None:
                return None
        if atual == self.primeiro:
            self.primeiro = atual.proximo
        else:
            atual.anterior.proximo = atual.proximo
            
        if atual == self.ultimo:
            ultimo = atual.anterior
        else:
            atual.proximo.anterior = atual.anterior
        
        return atual

    # Mostrar
    def mostrar_inicio(self):
        atual = self.primeiro
        
        while atual != None:
            atual.mostra_no()
            atual = atual.proximo
            
    def mostrar_final(self):
        atual = self.ultimo
        
        while atual != None:
            atual.mostra_no()
            atual = atual.anterior