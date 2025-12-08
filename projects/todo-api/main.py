def ler_numero(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            return valor
        except ValueError:
            print("Valor inválido. Tente novamente.")


def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b


def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b == 0:
        print("Erro: divisão por zero!")
        return None
    return a / b


def mostrar_menu():
    print("\n=== CALCULADORA ===")
    print("1) Somar")
    print("2) Subtrair")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "5":
            print("Saindo... Até mais!")
            break

        if opcao not in ("1", "2", "3", "4"):
            print("Opção inválida. Tente de novo.")
            continue

        x = ler_numero("Digite o primeiro número: ")
        y = ler_numero("Digite o segundo número: ")

        if opcao == "1":
            resultado = somar(x, y)
            operacao = "+"
        elif opcao == "2":
            resultado = subtrair(x, y)
            operacao = "-"
        elif opcao == "3":
            resultado = multiplicar(x, y)
            operacao = "*"
        else:  # opcao == "4"
            resultado = dividir(x, y)
            operacao = "/"

        if resultado is not None:
            print(f"\n{x} {operacao} {y} = {resultado}")


if __name__ == "__main__":
    main()
