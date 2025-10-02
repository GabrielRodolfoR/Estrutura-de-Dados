def contagem_digitos_numeros(lista):
    if not lista:
        return []
    n = lista[0]

    def contar_digitos(n):
        if n < 10:
            return 1
        else:
            return 1 + contar_digitos(n // 10)

    return [contar_digitos(n)] + contagem_digitos_numeros(lista[1:])


def somar_elementos_lista(lista):
    if not lista:
        return 0
    else:
        return lista[0] + somar_elementos_lista(lista[1:])


def verificar_palindromo(lista):
    if len(lista) <= 1:
        return True
    if lista[0] != lista[-1]:
        return False
    return verificar_palindromo(lista[1:-1])


def desenhar_triangulo_asteristicos(lista):
    if not lista:
        return
    n = lista[0]
    for linha in range(1, n + 1):
        print("*" * linha)
    print()
    desenhar_triangulo_asteristicos(lista[1:])


def criar_lista():
    lista = []
    print("Digite números inteiros positivos para a lista. Digite -1 para terminar.")
    while True:
        try:
            valor = int(input("Digite um número (ou -1 para terminar): "))
            if valor == -1:
                break
            elif valor < 0:
                print(
                    "Por favor, digite apenas números inteiros positivos ou -1 para terminar."
                )
                continue
            else:
                lista.append(valor)
        except ValueError:
            print("Entrada inválida. Digite um número inteiro.")
    return lista


while True:
    print(
        "=====Escolha uma opção ====="
        "\n1 - Contagem de Dígitos em uma lista de números"
        "\n2 - Somar Elementos de uma lista"
        "\n3 - Verificar Palíndromo em uma lista"
        "\n4 - Desenhar um Triângulo de Asteriscos para cada número da lista"
        "\n5 - Sair"
    )
    try:
        escolha = int(input("Digite um valor: "))
    except ValueError:
        print("Por favor, digite um número válido.")
        continue

    if escolha == 1:
        lista = criar_lista()
        resultado = contagem_digitos_numeros(lista)
        print("Contagem de dígitos para cada número:", resultado)

    elif escolha == 2:
        lista = criar_lista()
        resultado = somar_elementos_lista(lista)
        print("Soma dos elementos da lista:", resultado)

    elif escolha == 3:
        lista = criar_lista()
        resultado = verificar_palindromo(lista)
        if resultado:
            print("A lista é um palíndromo.")
        else:
            print("A lista não é um palíndromo.")

    elif escolha == 4:
        lista = criar_lista()
        desenhar_triangulo_asteristicos(lista)

    elif escolha == 5:
        print("Saindo...")
        break

    else:
        print("Opção Inválida!")
