"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = Identidade
"""
condicao = False
passou_no_if = None

if condicao:
    passou_no_if = True
    print('Faça algo')
else:
    print('Não faça algo')

# no lugar do is também pode ser usado o == mas para none, o ideal é is
if passou_no_if is None:
    print('Não passou no if')
else:
    print('Passou no if')
