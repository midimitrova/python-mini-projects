import random


def dice_rolling():
    dice_art = {
        1: (
            "┌─────────┐",
            "│         │",
            "│    ●    │",
            "│         │",
            "└─────────┘",
        ),
        2: (
            "┌─────────┐",
            "│  ●      │",
            "│         │",
            "│      ●  │",
            "└─────────┘",
        ),
        3: (
            "┌─────────┐",
            "│  ●      │",
            "│    ●    │",
            "│      ●  │",
            "└─────────┘",
        ),
        4: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│         │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        5: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│    ●    │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
        6: (
            "┌─────────┐",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "│  ●   ●  │",
            "└─────────┘",
        ),
    }

    roll = input('Roll the dice? (Yes/No): ').strip().lower()

    while roll != 'No'.lower():
        if roll == 'Yes'.lower():
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)

            print(f'Dice rolled {dice1} and {dice2}.')
            print('\n'.join(dice_art[dice1]))
            print('\n'.join(dice_art[dice2]))

            roll = input('Roll again? (Yes/No): ')
        else:
            if roll not in ['Yes'.lower(), 'No'.lower()]:
                print('Invalid response. Please, type Yes or No: ')
                roll = input('Roll the dice? (Yes/No): ').strip().lower()


dice_rolling()
print('Thank you for playing!')
