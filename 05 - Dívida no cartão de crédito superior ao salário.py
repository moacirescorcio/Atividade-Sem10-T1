salario = float(input('Insira o valor do salário: '))
divida = float(input('Insira o valor da dívida: '))
mes = 10
ano = 2016

while salario > divida:    
    divida  = (divida * 0.15) + divida
    mes += 1
    if mes == 13:        
        mes = 1
        ano += 1
    if mes == 3:
            salario = (salario * 0.05) + salario

print(f'A dívida vai superar o salário em {mes}/{ano}')
