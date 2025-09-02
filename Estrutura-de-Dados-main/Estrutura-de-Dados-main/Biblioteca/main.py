from biblioteca import Biblioteca
from livro import Livro
from usuario import Usuario


class Main:
    def __init__(self):
        self.biblioteca = Biblioteca("Biblioteca Central")
        self.usuarios = []
        self.livros = []

    def menu(self):
        while True:
            try:
                opcao = int(
                    input(
                        "========== Menu =========="
                        "\n1- Usuários"
                        "\n2- Livros"
                        "\n3- Biblioteca"
                        "\n4- Sair"
                        "\nSelecione: "
                    )
                )
            except ValueError:
                print("Inválido! Digite um número.")
                continue

            if opcao == 1:
                nome = input("Digite o nome do usuário: ")
                self.usuarios.append(Usuario(nome))
                print(f"Usuário '{nome}' cadastrado com sucesso!")

            elif opcao == 2:
                if not self.biblioteca.livros:
                    print("Nenhum livro cadastrado.")
                else:
                    for i, livro in enumerate(self.biblioteca.livros, start=1):
                        print(f"{i} - {livro.titulo}")
                    try:
                        escolha = int(
                            input("Selecione o número do livro para detalhes: ")
                        )
                        if 1 <= escolha <= len(self.biblioteca.livros):
                            self.biblioteca.livros[escolha - 1].exibirDetalhes()
                        else:
                            print("Opção inválida.")
                    except ValueError:
                        print("Digite um número válido.")

            elif opcao == 3:
                try:
                    new_opcao = int(
                        input(
                            "========== Menu Biblioteca =========="
                            "\n1- Adicionar Novo Livro"
                            "\n2- Visualizar lista de Livros"
                            "\nSelecione: "
                        )
                    )
                except ValueError:
                    print("Inválido! Digite um número.")
                    continue

                if new_opcao == 1:
                    titulo = input("Título: ")
                    autor = input("Autor: ")
                    livro = Livro(titulo, autor)
                    self.biblioteca.adicionarLivro(livro)

                elif new_opcao == 2:
                    print("========== Lista de Livros ==========")
                    print(self.biblioteca.exibirLivrosDisponiveis())

            elif opcao == 4:
                break


if __name__ == "__main__":
    main = Main()
    main.menu()
