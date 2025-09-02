from vetor_nao_ordenado import VetorNaoOrdenado

class Main:
    def __init__(self):
        self.capacidade = int(input("Capacidade: "))
        self.vetor = VetorNaoOrdenado(self.capacidade)

    def menu(self):
        while True:
            print("========== Menu de Opções ==========")
            opcao = int(
                input(
                    "1 - Inserir"
                    "\n2 - Imprimir"
                    "\n3 - Pesquisar"
                    "\n4 - Excluir"
                    "\n5 - Sair"
                    "\nEscolha: "
                )
            )

            if opcao == 1:
                print("========== Inserir ==========")
                valor = input("Valor: ")
                self.vetor.inserir(valor)
                
            elif opcao == 2:
                print("========== Imprimir ==========")
                self.vetor.imprimir()
                
            elif opcao == 3:
                print("========== Pesquisar ==========")
                valor = input("Valor: ")
                print(self.vetor.pesquisar(valor))
                
            elif opcao == 4:
                print("========== Excluir ==========")
                valor = input("Valor: ")
                
                self.vetor.excluir(valor)
            elif opcao == 5:
                break
            
            else:
                print("Valor Inválido!!")

if __name__ == "__main__":
    app = Main()
    app.menu()
