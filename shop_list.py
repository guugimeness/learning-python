# Exercício: lista de compras
import os

shop_list = []
value = ''
index = 0
option = ''
valid_options = 'ials'

while option != 's':
    
    print('[i]nserir | [a]pagar | [l]istar | [s]air')
    option = input('Selecione uma opção: ')
    
    os.system('clear')
    
    if option not in valid_options:
        print('Por favor, selecione uma opção válida!')
        continue
    
    if option == 's':
        break
    elif option == 'i':
        value = input('Item: ')
        shop_list.append(value)
    elif option == 'a':
        index = input('Escolha o índice para apagar: ')
        try:
            index_int = int(index)
            del shop_list[index_int]
        except ValueError:
            print('Digite um número inteiro!')
        except IndexError:
            print('Esse índice não existe na lista!')
        except Exception:
            print('Erro desconhecido')
    else:
        if not shop_list:
            print('A lista está vazia no momento!')
        else:
            for index, item in enumerate(shop_list):
                print(f'[{index}] - {item}')
            print()
