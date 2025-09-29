"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Luiz'
preco = 1000.95897643

# método format
variavel = '%s, o preço é R$ %.2f' % (nome, preco)
print(variavel)

# método f string
variavel = f'{nome}, o preço é R$ {preco:.2f}'
print(variavel)

# o 08 dessa parte %08X significa acrescentar 8 zeros
print('O hexadecimal de %d é %08X' % (1500, 1500))
