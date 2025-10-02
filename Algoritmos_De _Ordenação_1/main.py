import random


def bubble_sort():
    n = len(array)

    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

    return array


def insertion_sort():
    n = len(array)

    for i in range(n):
        marcado = array[i]
        j = i - 1

        while j >= 0 and marcado < array[j]:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = marcado

    return array


while True:
    print(
        "=====Escolha uma opção ====="
        "\n1 - Usar lista com 1000 números"
        "\n2 - Usar lista de nomes"
    )
    try:
        escolha = int(input("Digite 1 ou 2: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if escolha == 1:
        array = list(range(1, 1001))
        random.shuffle(array)
        print(f"Lista Original: {array}")
    elif escolha == 2:
        array = [
            "Alice Silva",
            "Bruno Oliveira",
            "Carla Santos",
            "Daniel Costa",
            "Elisa Fernandes",
            "Fabio Souza",
            "Gabriela Lima",
            "Henrique Almeida",
            "Isabel Ribeiro",
            "JoÃ£o Pereira",
            "Karla Nogueira",
            "Leonardo Mendes",
            "Mariana Castro",
            "Nina Cardoso",
            "OtÃ¡vio Rocha",
            "PatrÃ­cia Barros",
            "Quintino Guedes",
            "Rafael Martins",
            "Sofia Neves",
            "Tiago Alves",
            "Ursula Morais",
            "Victor Correia",
            "Wagner Braga",
            "Xavier Mendes",
            "Yasmin Vieira",
            "ZÃ©lia Figueiredo",
            "Adriana Ramos",
            "Bernardo Lopes",
            "CecÃ­lia Freitas",
            "Davi Borges",
            "Eduarda Farias",
            "Felipe Moreira",
            "Giovanna Carvalho",
            "Heitor Medeiros",
            "InÃªs Duarte",
            "Jorge Sales",
            "KauÃ£ Pinheiro",
            "Larissa Santana",
            "Miguel Dias",
            "NatÃ¡lia Cruz",
            "Otto Camargo",
            "Pedro Gouveia",
            "Quirino Andrade",
            "Renata Paiva",
            "Samuel AraÃºjo",
            "Tereza Maia",
            "Ulisses Monteiro",
            "Vanessa Rocha",
            "Willian Ribeiro",
            "Ximena Cardoso",
            "Yuri MagalhÃ£es",
            "Amanda Souza",
            "Bruna Ferreira",
            "Camila Duarte",
            "Diego Barbosa",
            "Eduardo Lima",
            "Fernanda Machado",
            "Giovani Costa",
            "Helena Silva",
            "Ian Farias",
            "Jessica Teixeira",
            "Kaique AraÃºjo",
            "Laura Gomes",
            "Marcelo Vieira",
            "Nicolas Souza",
            "Olga Albuquerque",
            "Paulo Reis",
            "Quintino Martins",
            "Rodrigo Costa",
            "Sara Fonseca",
            "Tatiane Andrade",
            "Ubirajara Santos",
            "Vicente Tavares",
            "Wesley Lopes",
            "Xande Cruz",
            "Yara Morais",
            "Ãgata Santos",
            "Breno Albuquerque",
            "CÃ©sar Teixeira",
            "Douglas Lima",
            "Emanuel Almeida",
            "FlÃ¡via Pinto",
            "Gustavo Cunha",
            "Helder Martins",
            "Igor Ribeiro",
            "Juliana Alves",
            "Karen Silva",
            "Leandro Azevedo",
            "MaitÃª Cardoso",
            "Nilson Pereira",
            "Oscar Ribeiro",
            "PatrÃ­cia Gomes",
            "Quintino Ferreira",
            "Rita AraÃºjo",
            "Simone Costa",
            "TomÃ¡s Almeida",
            "Ursula Monteiro",
            "Vitor Gomes",
            "Wellington Alves",
            "Xena Ramos",
            "Yuri Reis",
            "Anita Silva",
            "Bianca Barros",
            "Carlos Teixeira",
            "Diana Costa",
            "Elias Martins",
            "Fabiana Freitas",
            "Gabriel Almeida",
            "Heloisa Ribeiro",
            "Igor Lima",
            "Joana Pereira",
            "KlÃ©ber Cardoso",
            "Lucas Nogueira",
            "Mara Souza",
            "Nelson Cunha",
            "OtÃ¡vio Barros",
            "Priscila Alves",
            "Quirino Duarte",
            "Ricardo Gomes",
            "Sabrina Oliveira",
            "Thales Martins",
            "Ubiratan Vieira",
            "Valentina Ferreira",
            "Wanderley Mendes",
            "XÃªnia Lopes",
            "Yasmin Azevedo",
            "Aline Ramos",
            "Beatriz Silva",
            "Cristiano Cardoso",
            "Daniela Barros",
            "Eduardo Santos",
            "FÃ¡bio Freitas",
            "Giovana Costa",
            "Heitor Reis",
            "Isabela Lima",
            "JÃºlio Vieira",
            "Karina Oliveira",
            "Luan Ribeiro",
            "Marcela Souza",
            "Natasha Pereira",
            "Orlando Almeida",
            "Paola Santos",
            "Quirino Martins",
            "Roberta Mendes",
            "SÃ©rgio Cardoso",
            "Tatiana Ramos",
            "Ulisses Martins",
            "Vanessa Souza",
            "William Ferreira",
            "Ximena Alves",
            "Yago Cruz",
            "AndrÃ© Almeida",
            "Bruno Santos",
            "Carla Reis",
            "Diego Costa",
            "Eduarda Souza",
            "Felipe Oliveira",
            "Gustavo Lima",
            "Helena Mendes",
            "Igor Cardoso",
            "Julia Freitas",
            "Karla Martins",
            "Leonardo Costa",
            "Mariana Lopes",
            "Nicolas Mendes",
            "Olga Souza",
            "Paulo Cardoso",
            "Quirino Barros",
            "Rafael Andrade",
            "Silvia Mendes",
            "Thiago Neves",
            "Ursula Teixeira",
            "Vitor Cardoso",
            "William Ribeiro",
            "XÃªnia Andrade",
            "Yara Costa",
            "Ãlvaro Martins",
            "BÃ¡rbara Souza",
            "Alexandre Braga",
            "Benedito Lopes",
            "Caio Neves",
            "Dalila Souza",
            "Emerson Oliveira",
            "Fernanda Barros",
            "Guilherme Teixeira",
            "Hugo Rocha",
            "Ingrid Ramos",
            "JoÃ£o Victor",
            "Kevin Santos",
            "LÃ­via Costa",
            "Marcos Freitas",
            "Neusa Alves",
            "Olavo Rocha",
            "Paulo Henrique",
            "Querubina Souza",
            "Ronaldo Nogueira",
            "Simone Teixeira",
            "Tales Barros",
            "Uliana Santos",
            "VinÃ­cius Ramos",
        ]
    else:
        print("Opção inválida. Tente novamente.")
        continue

    print(
        "===== Escolha o tipo de ordenação ====="
        "\n1 - Bubble Sort"
        "\n2 - Insertion Sort"
    )

    try:
        opcao = int(input("Digite 1 ou 2: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if opcao == 1:
        print("===== Bubble Sort =====")
        bubble_sort()

    elif opcao == 2:
        print("===== Insertion Sort =====")
        insertion_sort()

    else:
        print("Opção inválida. Tente novamente.")
        continue

    print("Array ordenado:")
    print(array)

    continuar = input("\nDeseja ordenar novamente? (s/n): ").strip().lower()

    if continuar != "s":
        print("Programa finalizado.")
        break
