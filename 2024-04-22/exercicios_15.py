###15. Receba 3 números inteiros na entrada e imprima: crescente, se eles forem dados em ordem 
### crescente. Caso contrário, imprima não está em ordem crescente.

# Leia três números inteiros
numero1 = int(input("Digite o primeiro número inteiro: "))
numero2 = int(input("Digite o segundo número inteiro: "))
numero3 = int(input("Digite o terceiro número inteiro: "))

# Verifique se os números estão em ordem crescente
if numero1 < numero2 < numero3:
    print("Crescente")
else:
    print("Não está em ordem crescente.")