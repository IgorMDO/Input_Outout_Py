# Data input and output

nome = input("Insira seu nome\n")
n1 = input(f'Insira sua primeira nota, {nome}\n')
n2 = input(f'Insira a segunda nota, {nome}\n')
n3 = input(f'Por fim, insira a última nota.\n')
media = (int(n1) + int(n2) + int(n3)) / 3

print(f'A média entre os valores: {n1}, {n2}, {n3} é igual a {media}')
#obs: A variável nome, neste código é descartável, ou seja, há completa execução do código mesmo com sua retirada
