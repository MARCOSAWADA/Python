### 22. Escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. 
### Isto é, domingo equivale a 1, segunda-feira se 2, e assim por diante.

# Ler um inteiro entre 1 e 7
numero = int(input("Digite um número entre 1 e 7: "))

# Verificar o dia da semana correspondente
if numero == 1:
    print("Domingo")
elif numero == 2:
    print("Segunda-feira")
elif numero == 3:
    print("Terça-feira")
elif numero == 4:
    print("Quarta-feira")
elif numero == 5:
    print("Quinta-feira")
elif numero == 6:
    print("Sexta-feira")
elif numero == 7:
    print("Sábado")
else:
    print("Número inválido. Por favor, insira um número entre 1 e 7.")