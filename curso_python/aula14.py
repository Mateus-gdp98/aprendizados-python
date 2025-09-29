a = 'AAAAA'
b = 'BBBBBB'
c = 1.1

# dentro das {} estão os parâmetros definidos depois
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'

# definindo nome de parâmetro e atribuindo eles a variável
formato = string.format(
    nome1=a, nome2=b, nome3=c
)

print(formato)
