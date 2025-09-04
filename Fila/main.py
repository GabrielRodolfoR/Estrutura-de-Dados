from fila import Fila


class Main:
    def __init__(self):
        self.capacidade = int(input("Capacidade: "))
        self.vetor = Fila(self.capacidade)

    def menu(self):
        while True:
            print("========== Menu de Opções ==========")
            opcao = int(
                input(
                    "1 - Fila Cheia"
                    "\n2 - Enfileirar"
                    "\n3 - Fila Vazia"
                    "\n4 - Desenfileirar"
                    "\n5 - Primeiro"
                    "\n6 - Sair"
                    "\nEscolha: "
                )
            )

            if opcao == 1:
                print("========== Fila Cheia ==========")
                print(f"Status: {self.vetor.fila_cheia()}")

            elif opcao == 2:
                print("========== Enfileirar ==========")
                valor = input("Valor: ")
                self.vetor.enfileirar(valor)

            elif opcao == 3:
                print("========== Fila Vazia ==========")
                print(f"Status: {self.vetor.fila_vazia()}")

            elif opcao == 4:
                print("========== Desenfileirar ==========")
                print(self.vetor.desenfileirar())

            elif opcao == 5:
                print("========== Primeiro ==========")
                print(f"Primeiro Item: {self.vetor.primeiro()}")

            elif opcao == 6:
                break

            else:
                print("Valor Inválido!!")


if __name__ == "__main__":
    app = Main()
    app.menu()
