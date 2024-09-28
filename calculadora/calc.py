def calculadora(num1, num2, operacao):
    if operacao == 1:
        return num1 + num2  # Soma
    elif operacao == 2:
        return num1 - num2  # Subtração
    elif operacao == 3:
        return num1 * num2  # Multiplicação
    elif operacao == 4:
        if num2 != 0:
            return num1 / num2  # Divisão
        else:
            return "Erro: Divisão por zero!"
    else:
        return 0  # Operação inválida

# Exemplos de uso:
num1 = 10
num2 = 5
operacao = 3  # Operação de soma

resultado = calculadora(num1, num2, operacao)
print(f"O resultado é: {resultado}")
