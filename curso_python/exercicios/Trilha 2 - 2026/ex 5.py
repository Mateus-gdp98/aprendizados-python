'''
#Dia 2 — Exercício 5

O programa deve pedir:

nome
idade
experiência profissional (S/N)
curso técnico ou superior (S/N)

Depois, classifique a pessoa:

Aprovado -> Se: idade ≥ 18 E possui experiência E possui curso
Em análise -> Se: idade ≥ 18 E possui experiência OU possui curso
Reprovado -> Se não atender aos critérios anteriores.

'''
# =====================================================================
try:
    pessoa = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    experiencia = input("Você tem experiência profissional? (S/N): ").upper()
    formacao =  input("Você possui curso técnico ou superior? (S/N): ").upper()

    if idade >= 18 and experiencia == "S" and formacao =="S":
        print("🟢 Aprovado")
    elif idade >= 18 and (experiencia == "S" or formacao =="S"):
        print("🟡 Em análise")
    else:
        print("🔴 Reprovado")

except:
    print("Dados inválidos.")