#  Faça um algoritmo que receba o número de avaliações do estudante
#  que será (utilizado como contador), após receba as notas e
# apresente a média do estudante.


num_avaliacoes = int(input("Digite o número de avaliações: "))

# Inicializa a variável para armazenar a soma das notas
soma_notas = 0


for i in range(num_avaliacoes):
    nota = float(input(f"Digite a nota {i + 1}: "))
    soma_notas = soma_notas + nota


media = soma_notas / num_avaliacoes


print("A média do estudante é: " , media)
