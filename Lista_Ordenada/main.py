from vetor_ordenado import VetorOrdenado

class Main:
    def __init__(self):
        self.capacidade = int(input("Capacidade: "))
        self.vetor = VetorOrdenado(self.capacidade)

    def menu(self):
        while True:
            print("========== Menu de Opções ==========")
            opcao = int(
                input(
                    "1 - Inserir"
                    "\n2 - Imprimir"
                    "\n3 - Pesquisa_linear"
                    "\n4 - pesquisa_binaria"
                    "\n5 - Excluir"
                    "\n6 - Sair"
                    "\nEscolha: "
                )
            )

            if opcao == 1:
                print("========== Inserir ==========")
                valor = int(input("Valor: "))
                self.vetor.inserir(valor)
                
            elif opcao == 2:
                print("========== Imprimir ==========")
                self.vetor.imprimir()
                
            elif opcao == 3:
                print("========== Pesquisa Linear ==========")
                valor = int(input("Valor: "))
                print(self.vetor.pesquisa_linear(valor))
                
            elif opcao == 4:
                print("========== Pesquisa Binária ==========")
                valor = int(input("Valor: "))
                print(self.vetor.pesquisa_binaria(valor))
                
            elif opcao == 5:
                print("========== Excluir ==========")
                valor = int(input("Valor: "))
                
                self.vetor.excluir(valor)
            elif opcao == 6:
                break
            
            else:
                print("Valor Inválido!!")

if __name__ == "__main__":
    app = Main()
    app.menu()
