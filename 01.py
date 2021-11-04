def quantos_anos(d, j):
    quantidade = 0
    while d > 0 and j > 0:
        d * j == 2*d
        quantidade += 1

    return quantidade




deposito_inicial = float(input())
juros = float(input())
anos = quantos_anos(deposito_inicial, juros)
print(anos)