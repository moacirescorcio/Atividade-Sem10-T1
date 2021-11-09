def numero_invertido(n):
    invertido = 0
    while n > 0:
        invertido = (invertido * 10) + n % 10
        n = n // 10
    return invertido

n = int(input())
invertido = numero_invertido(n)
print(invertido)