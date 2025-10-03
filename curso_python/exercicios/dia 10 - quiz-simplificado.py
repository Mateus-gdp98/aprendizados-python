print('Quem quer ser um milionário 🤑')
print('-' * 90)

# dicionário de perguntas
perguntas = {
    "Qual é a capital da Austrália?": {
        "alternativas": ["A. Perth", "B. Sydney", "C. Melbourne", "D. Canberra"],
        "resposta": "d"
    },
    "O Monte Everest, a montanha mais alta do mundo, está localizado em qual cadeia de montanhas?": {
        "alternativas": ["A. Andes", "B. Alpes", "C. Himalaia", "D. Montanhas Rochosas"],
        "resposta": "c"
    },
    "Qual é o único planeta do sistema solar que gira no sentido horário?": {
        "alternativas": ["A. Vênus", "B. Marte", "C. Júpiter", "D. Saturno"],
        "resposta": "a"
    }
}

# contador de acertos
acertos = 0

# loop nas perguntas
for pergunta, dados in perguntas.items():
    print(pergunta)
    for alternativa in dados["alternativas"]:
        print(alternativa)
    print('-' * 90)

    resposta = input("Digite a alternativa correta: ").lower()

    if resposta == dados["resposta"]:
        print("Correto 🎉")
        acertos += 1
    else:
        print("Incorreto 😔")
    print('-' * 90)

print(f"Você teve um total de {acertos} acertos.")
