# Exercício: calculadora com while

option = ''

while option != 'sim':
    
    calculation = input('Digite a conta (número [+-*/] número): ').split()
    
    if len(calculation) == 3:
        value_1 = calculation[0]
        operator = calculation[1]
        value_2 = calculation[2]
    else:
        print('Por favor, digite a conta na formatação indicada!')
        continue
    
    try:
        num_1 = float(value_1)
        num_2 = float(value_2)
    except ValueError:
        print('Por favor, digite valores válidos!')
        continue
    
    valid_operators = '+-x/'
    
    if operator not in valid_operators:
        print('Por favor, digite um operador válido!')
        continue
    
    if operator == '+':
        result = num_1 + num_2
        print(f'{num_1} + {num_2} = {result:.3f}')
    elif operator == '-':
        result = num_1 - num_2
        print(f'{num_1} - {num_2} = {result:.3f}')
    elif operator == 'x':
        result = num_1 * num_2
        print(f'{num_1} x {num_2} = {result:.3f}')
    else:
        result = num_1 / num_2
        print(f'{num_1} / {num_2} = {result:.3f}')
    
    option = input('Quer sair? Digite "sim"; caso contrário, digite qualquer coisa. ')