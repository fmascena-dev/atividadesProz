def calculadora():
    while True:
        # Exibe o menu de operações
        print("\nEscolha uma operação:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Solicita a operação do usuário
        operacao = input("Digite o número da operação: ")

        if operacao == '0':
            print("Saindo do programa...")
            break  # Encerra o loop e o programa
        elif operacao in ['1', '2', '3', '4']:
            try:
                # Solicita os números
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                # Executa a operação escolhida
                if operacao == '1':
                    resultado = num1 + num2
                    print(f"Resultado: {num1} + {num2} = {resultado}")
                elif operacao == '2':
                    resultado = num1 - num2
                    print(f"Resultado: {num1} - {num2} = {resultado}")
                elif operacao == '3':
                    resultado = num1 * num2
                    print(f"Resultado: {num1} * {num2} = {resultado}")
                elif operacao == '4':
                    if num2 != 0:
                        resultado = num1 / num2
                        print(f"Resultado: {num1} / {num2} = {resultado}")
                    else:
                        print("Erro: Divisão por zero não é permitida.")
            except ValueError:
                print("Erro: Por favor, insira números válidos.")
        else:
            print("Essa opção não existe, tente novamente.")

# Chamada da função
calculadora()
