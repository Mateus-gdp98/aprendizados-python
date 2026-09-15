'''
Dia 1 — Exercício 2

Faça um programa que receba:

nome
idade
salário mensal

E calcule:

salário anual;
salário mensal + 10% de aumento;
novo salário anual.

'''
# =====================================================================
try:
    pessoa = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    salario_atual = float(input("Digite o salário da pessoa: "))
    salario_anual_atual = round(salario_atual * 12,2)
    
    salario_novo = round(salario_atual + (salario_atual * 0.10),2)
    salario_anual_novo = round(salario_novo * 12,2)

    print('-' * 90)
    print(f"Usuário {pessoa}, possui {idade} anos. \nSeu salário mensal atual é R$ {salario_atual}, porém, ele recebeu um aumento de 10%, o que atualiza seu salário para R$ {salario_novo} e anualmente fica em torno de R$ {salario_anual_novo}")

except:
    print("Digite valores válidos.")
    print('-' * 90)