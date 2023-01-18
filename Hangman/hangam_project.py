import random
from words import words_list

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
lives = 6

used_letters = []

chosen_word = random.choice(words_list)

display = []
underscore = '_'
for letter in chosen_word:
    display.append(underscore)
print(f'{" ".join(display)}')

while True:
    user_input = input('Guess a letter: ').lower().strip()

    if not user_input.isalpha():
        print('Invalid character! Please, try again!\n')
        continue
    if user_input in used_letters:
        print('You have already used that letter. Guess another letter.\n')
        continue
    else:
        used_letters.append(user_input)

    for index_letter in range(len(chosen_word)):
        if user_input == chosen_word[index_letter]:
            display[index_letter] = user_input
    if user_input not in chosen_word:
        lives -= 1
        print(f'{user_input} is not in the word. You have {lives} lives left.\n')
        if lives == 0:
            print('You lose the game!')
            print(f'The word is {chosen_word}.')
            print(stages[lives])
            break

    if '_' not in display:
        print('You win the game!')
        break

    print(f'{" ".join(display)}')
    print(stages[lives])
    print(f'You use these letters: {", ".join(used_letters)}\n')
