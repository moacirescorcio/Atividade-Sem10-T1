lista = []
while True:
    n = int(input('Insira um número (digite "0" para encerrar): '))
    if n > 0:
        lista.append(n)
    if n == 0:         
        break


maior = max(lista)
menor = min(lista)
print(f'O maior valor é {maior}')
print(f'O menor valor é {menor}')
