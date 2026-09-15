'''
#Dia 1 — Exercício 4

Agora quero que você faça um programa que receba:

nome
idade
salário

E classifique a pessoa em três faixas etárias:

menor de 18 → Menor de idade
18 até 59 → Adulto
60 ou mais → Idoso

E, separadamente, classifique o salário:

abaixo de R$ 2.000 → Faixa salarial baixa
de R$ 2.000 até R$ 5.000 → Faixa salarial média
acima de R$ 5.000 → Faixa salarial alta

'''
# =====================================================================
try:
    pessoa = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    salario_atual = float(input("Digite o salário da pessoa: "))
    print('-' * 90)

    if idade < 18:
        print(f"É menor de idade, possui {idade} anos.")

    elif idade >= 18 and idade <= 59:
        print(f"É adulto, possui {idade} anos.")

    else:
        print(f"É idoso, possui {idade} anos.")


    if salario_atual < 2000:
        print(f"Faixa salarial baixa | Salário de R$ {salario_atual}")

    elif salario_atual >= 2000 and salario_atual <= 5000:
        print(f"Faixa salarial média | Salário de R$ {salario_atual}")

    else:
        print(f"Faixa salarial alta | Salário de R$ {salario_atual}")

    print('-' * 90)

except:
    print("Digite valores válidos.")
    print('-' * 90)