### 12. Crie um programa que receba um número inteiro e verifique se este número é par ou ímpar.


numero = int(input("Digite um número inteiro: "))


if numero % 2 != 0:
    print(numero, "é um número par.")
else:
    print(numero, "é um número ímpar.")