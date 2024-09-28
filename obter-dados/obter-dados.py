def obter_dados_usuario():
    # Solicita o nome completo do usuário
    nome = input("Digite seu nome completo: ")

    while True:
        try:
            # Solicita o ano de nascimento do usuário
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))

            # Verifica se o ano está dentro do intervalo válido
            if 1922 <= ano_nascimento <= 2021:
                idade = 2022 - ano_nascimento
                print(f"Nome: {nome}")
                print(f"Você completou, ou completará, {idade} anos em 2022.")
                break
            else:
                print("Erro: O ano deve estar entre 1922 e 2021. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, digite um número válido.")

# Chama a função para iniciar o programa
obter_dados_usuario()
