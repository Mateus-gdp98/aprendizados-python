#lista de números ao quadrado usando map e lambda
numeros = [1, 2, 3, 4, 5]
print(f'Os números são {numeros}')
print('-' * 60)

# usando lambda dentro do map
resultado = list(map(lambda n: n ** 2, numeros))

print(f'E o quadrado deles é {resultado}')
