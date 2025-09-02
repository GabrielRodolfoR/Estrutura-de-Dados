class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livrosEmprestados = []

    def emprestarLivro(self, livro):
        if livro.disponivel:
            livro.disponivel = False
            self.livrosEmprestados.append(livro)
            print(f"{self.nome} emprestou o livro '{livro.titulo}'.")
        else:
            print(f"O livro '{livro.titulo}' não está disponível.")

    def devolverLivro(self, livro):
        if livro in self.livrosEmprestados:
            livro.disponivel = True
            self.livrosEmprestados.remove(livro)
            print(f"{self.nome} devolveu o livro '{livro.titulo}'.")
        else:
            print("Este livro não foi emprestado por este usuário.")
