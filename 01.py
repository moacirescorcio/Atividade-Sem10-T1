deposito = float(input('Insira o valor do depósito: '))
juros = float(input('Insira o valor do juros: '))
quantidade = 0
objetivo = 2 * deposito
montante = 0
while montante < objetivo:        
    montante = (deposito * (juros/100)) + deposito
    deposito = montante
    quantidade += 1        

print(f'Vai levar {quantidade} anos para dobrar o valor!')
        
        
        

