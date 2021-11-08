q = 0
num = 0
while True:
    n = int(input('Insira um número (digite "0" para parar): '))
    if n > 0:
        num += n    
        q += 1    
    else:
        break

if q > 0:
    media = num / q
    print(f'A média dos números é de {media:.2f}')
