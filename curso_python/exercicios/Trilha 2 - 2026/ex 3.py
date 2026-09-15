'''
Dia 1 — Exercício 3

Agora quero introduzir uma coisa que será fundamental para o restante do Python:

Condições

Faça um programa que receba:

nome
idade
salário

Depois:

Se a idade for 18 ou mais, informe que a pessoa é maior de idade.
Se for menor que 18, informe que é menor de idade.
Se o salário for maior ou igual a R$ 3.000, informe que está acima do limite definido.
Caso contrário, informe que está abaixo desse limite.

'''
# =====================================================================
try:
    pessoa = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    salario_atual = float(input("Digite o salário da pessoa: "))
    print('-' * 90)

    if idade >= 18:
        print(f"É maior de idade, possui {idade} anos.")
    else:
        print(f"É menor de idade, possui {idade} anos.")

    if salario_atual >= 3000:
        print(f"Alerta, está acima do limite (R$ 3.000,00), salário de R$ {salario_atual}")
    else:
        print(f"Ok, está dentro do limite (R$ 3.000,00), salário de R$ {salario_atual}")

    print('-' * 90)

except:
    print("Digite valores válidos.")
    print('-' * 90)