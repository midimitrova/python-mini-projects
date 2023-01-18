import random
from art import logo


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare(user_score, computer_score):
    if user_score == computer_score:
        return 'Draw.\n'
    elif computer_score == 0:
        return 'Lose, opponent has Blackjack.\n'
    elif user_score == 0:
        return 'You win with a Blackjack.\n'
    elif user_score > 21:
        return 'You went over. You lose.\n'
    elif computer_score > 21:
        return 'Opponent went over. You win.\n'
    elif user_score > computer_score:
        return 'You win.\n'
    else:
        return 'You lose.\n'


def blackjack():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f'    Your cards: {" ".join(map(str, user_cards))}, current score: {user_score}')
        print(f'    Computer\'s first card: {computer_cards[0]}')

        if user_score == 0 or user_score > 21 or computer_score == 0:
            is_game_over = True
        else:
            user_input = input("Type 'y' to get another card, type 'n' to pass.: ").strip().lower()
            if user_input == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f'    Your final hand: {" ".join(map(str, user_cards))}, final score: {user_score}')
    print(f'    Computer\'s final hand: {" ".join(map(str, computer_cards))}, final score: {computer_score}')
    print(compare(user_score, computer_score))


while True:
    question_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if question_to_play == 'y':
        blackjack()
    else:
        break
