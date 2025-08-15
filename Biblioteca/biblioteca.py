class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionarLivro(self, livro):  # recebe o livro
        self.livros.append(livro)
        print(f"O livro '{livro.titulo}' foi adicionado com sucesso!")

    def exibirLivrosDisponiveis(self):
        if not self.livros:
            return "Sem livros cadastrados."

        for livro in self.livros:
            print(f"{livro.titulo} | {livro.autor} | {livro.disponivel}")
        return "Busca finalizada com sucesso!"
