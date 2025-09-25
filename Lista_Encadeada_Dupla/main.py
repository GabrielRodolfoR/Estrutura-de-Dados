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
                    "\n3 - Mostrar Início"
                    "\n4 - Mostrar Final"
                    "\n5 - Excluir Início"
                    "\n6 - Excluir Final"
                    "\n7 - Excluir Qualquer"
                    "\n8 - Sair"
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
                print("========== Mostrar Início ==========")
                self.lista.mostrar_inicio()

            elif opcao == 4:
                print("========== Mostrar Final ==========")
                self.lista.mostrar_final()

            elif opcao == 5:
                print("========== Excluir Início ==========")
                self.lista.excluir_inicio()

            elif opcao == 6:
                print("========== Excluir Final ==========")
                self.lista.excluir_final()

            elif opcao == 7:
                print("========== Excluir Qualquer ==========")
                valor = input("Valor a inserir: ")
                self.lista.excluir_qualquer(valor)

            elif opcao == 8:
                break

            else:
                print("Valor Inválido!!")


if __name__ == "__main__":
    app = Main()
    app.menu()
