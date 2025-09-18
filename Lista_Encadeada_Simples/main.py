from lista_encadeada_simples import ListaEncadeadaSimples
from no import No


class Main:
    def __init__(self):
        self.lista = ListaEncadeadaSimples()

    def menu(self):
        while True:
            print("========== Menu de Opções ==========")
            opcao = int(
                input(
                    "1 - Mostra No"
                    "\n2 - Inserir Inicio"
                    "\n3 - Mostrar"
                    "\n4 - Excluir Incio"
                    "\n5 - Pesquisar"
                    "\n6 - Excluir Qualquer"
                    "\n7 - Sair"
                    "\nEscolha: "
                )
            )

            if opcao == 1:
                print("========== Mostrar Nó ==========")
                valor = input("Valor do nó para mostrar: ")
                resultado = self.lista.pesquisar(valor)
                resultado.mostra_no()

            elif opcao == 2:
                print("========== Inserir Início ==========")
                valor = input("Valor a inserir: ")
                self.lista.inserir_inicio(valor)

            elif opcao == 3:
                print("========== Mostrar Lista ==========")
                self.lista.mostrar()

            elif opcao == 4:
                print("========== Excluir Início ==========")
                removido = self.lista.excluir_inicio()
                if removido:
                    print(f"Nó removido: {removido.valor}")
                else:
                    print("Lista vazia, nada a remover.")

            elif opcao == 5:
                print("========== Pesquisar ==========")
                valor = input("Valor a pesquisar: ")
                resultado = self.lista.pesquisar(valor)
                if resultado:
                    print(f"Valor encontrado: {resultado.valor}")
                else:
                    print("Valor não encontrado.")

            elif opcao == 6:
                print("========== Excluir Qualquer ==========")
                valor = input("Valor a excluir: ")
                removido = self.lista.excluir_qualquer(valor)
                if removido:
                    print(f"Nó removido: {removido.valor}")
                else:
                    print("Valor não encontrado para remoção.")

            elif opcao == 7:
                break

            else:
                print("Valor Inválido!!")


if __name__ == "__main__":
    app = Main()
    app.menu()
