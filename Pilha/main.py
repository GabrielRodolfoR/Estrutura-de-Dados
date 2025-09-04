from pilha import Pilha


class Main:
    def __init__(self):
        self.capacidade = int(input("Capacidade: "))
        self.vetor = Pilha(self.capacidade)

    def menu(self):
        while True:
            print("========== Menu de Opções ==========")
            opcao = int(
                input(
                    "1 - Pilha Cheia"
                    "\n2 - Empilhar"
                    "\n3 - Ver Topo"
                    "\n4 - Pilha Vazia"
                    "\n5 - Desempilhar"
                    "\n6 - Sair"
                    "\nEscolha: "
                )
            )

            if opcao == 1:
                print("========== Pilha Cheia ==========")
                print(f"Status: {self.vetor.pilha_cheia()}")

            elif opcao == 2:
                print("========== Empilhar ==========")
                valor = input("Valor: ")
                self.vetor.empilhar(valor)

            elif opcao == 3:
                print("========== Ver Topo ==========")
                print(f"Topo: {self.vetor.ver_topo()}")
                
            elif opcao == 4:
                print("========== Pilha Vazia ==========")
                print(f"Status: {self.vetor.pilha_vazia()}")

                
            elif opcao == 5:
                print("========== Desempilhar ==========")
                print(self.vetor.desempilhar())

            elif opcao == 6:
                break

            else:
                print("Valor Inválido!!")


if __name__ == "__main__":
    app = Main()
    app.menu()
