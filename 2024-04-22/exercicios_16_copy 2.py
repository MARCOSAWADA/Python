### 16. Crie um programa que leia 2 notas de um aluno, 
### verifique se as notas são válidas e exiba na tela a média destas notas. 
### Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, 
### onde caso a nota não possua um valor válido, este fato deve será informado ao usuário e o programa termina


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
    print("A média das notas é:", media)
else:
    print("Nota inválida. As notas devem estar entre 0.0 e 10.0.")