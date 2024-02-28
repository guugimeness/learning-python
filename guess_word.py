# Exercício: 
"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.
- Você vai propor uma palavra secreta qualquer e vai dar a possibilidade para o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você  vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta; exiba a letra;
    - Se a letra digitada não estiver na palavra secreta; exiba *.
- Faça a contagem de tentativas do seu usuário.
"""
import os

secret_word = list('Perfume')
user_word = []
attempts_count = 0

for letter in secret_word:
    user_word += '*'
    
while user_word != secret_word:
    
    current_letter = input('Digite uma letra: ')
    
    if not current_letter.isalpha() or len(current_letter) > 1:
        print('Você não digitou uma letra! Tente novamente')
        continue
    
    if current_letter in secret_word:
        index = 0
        while index < len(secret_word):
            if secret_word[index] == current_letter:
                user_word[index] = current_letter
            index += 1
        print(f'Palavra: {"".join(user_word)}')
    else:
        print(f'Palavra: {"".join(user_word)}')
    
    attempts_count += 1
else:
    os.system('clear')
    print()
    print('VOCÊ ACERTOU!!!')
    print(f'A palavra era "{"".join(secret_word)}"')
    print(f'Você precisou de {attempts_count} tentativas')