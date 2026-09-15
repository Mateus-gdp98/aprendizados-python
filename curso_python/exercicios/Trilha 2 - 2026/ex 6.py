'''
Dia 2 — Exercício 6

Sistema de login

O programa deve pedir:

usuário
senha

E verificar:

🟢 Acesso permitido -> Se: usuário correto E senha correta
🔴 Acesso negado -> Se qualquer uma das duas informações estiver errada.

'''
# =====================================================================
try:
    usuario_comum = "mateus"
    senha = 123

    login = input("Digite o seu login: ")
    senha_entrada = int(input("Digite a sua senha: "))

    if login == usuario_comum and senha_entrada == senha:
        print("🟢 Acesso comum")

    elif login == "gerente" or login == "admin":
        print("🟢 Acesso privilegiado")
        
    else:
        print("🔴 Acesso negado")

except:
    print("Dados inválidos.")