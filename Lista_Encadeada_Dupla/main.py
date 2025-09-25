from lista_encadeada_dupla import ListaEncadeadaDupla
from no import No


class Main:
    def __init__(self):
        self.lista = ListaEncadeadaDupla()

    def menu(self):
        while True:
            print("========== Menu de Opções ==========")
            opcao = int(
                input(
                    "\n1 - Inserir Inicio"
                    "\n2 - Inserir Final"
                    "\n3 - Pesquisar"
                    "\n4 - Mostrar Início"
                    "\n5 - Mostrar Final"
                    "\n6 - Excluir Início"
                    "\n7 - Excluir Final"
                    "\n8 - Excluir Qualquer"
                    "\n9 - Sair"
                    "\nEscolha: "
                )
            )

            if opcao == 1:
                print("========== Inserir Início ==========")
                valor = input("Valor a inserir: ")
                self.lista.inserir_inicio(valor)

            elif opcao == 2:
                print("========== Inserir Final ==========")
                valor = input("Valor a inserir: ")
                self.lista.inserir_final(valor)
            
            elif opcao == 3:
                print("========== Pesquisar ==========")
                valor = input("Valor a inserir: ")
                self.lista.pesquisar(valor)

            elif opcao == 4:
                print("========== Mostrar Início ==========")
                self.lista.mostrar_inicio()

            elif opcao == 5:
                print("========== Mostrar Final ==========")
                self.lista.mostrar_final()

            elif opcao == 6:
                print("========== Excluir Início ==========")
                self.lista.excluir_inicio()

            elif opcao == 7:
                print("========== Excluir Final ==========")
                self.lista.excluir_final()

            elif opcao == 8:
                print("========== Excluir Qualquer ==========")
                valor = input("Valor a inserir: ")
                self.lista.excluir_qualquer(valor)

            elif opcao == 9:
                break

            else:
                print("Valor Inválido!!")


if __name__ == "__main__":
    app = Main()
    app.menu()
