# Usando o for loop 
# Neste primeiro código, o laço for percorre os andares de 20 a 1. O número 13 é pulado usando continue.
for andar in range(20, 0, -1):
    if andar == 13:
        continue  # Pular o 13ro andar
    print(andar)


# Usando o while loop
# Neste segundo código, o laço while é usado para imprimir o andar atual e reduzir seu valor até chegar a 1. O número 13 também é pulado.
andar = 20
while andar > 0:
    if andar == 13:
        andar -= 1
        continue  # Pular o 13ro andar
    print(andar)
    andar -= 1


# Outro exemplo com while
# Neste terceiro código, o laço while funciona da mesma forma, mas a verificação de pular o andar 13 é feita diretamente no if sem o uso de continue.
andar = 20
while andar >= 1:
    if andar != 13:  # Só imprime se não for 13
        print(andar)
    andar -= 1
