quiz = {
    'question1': {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    'question2': {
        'question': 'What is the capital of Germany?',
        'answer': 'Berlin'
    },
    'question3': {
        'question': 'What is the capital of Italy?',
        'answer': 'Rome'
    },
    'question4': {
        'question': 'What is the capital of Spain?',
        'answer': 'Madrid'
    },
    'question5': {
        'question': 'What is the capital of Portugal?',
        'answer': 'Lisbon'
    },
    'question6': {
        'question': 'What is the capital of Switzerland?',
        'answer': 'Bern'
    },
    'question7': {
        'question': 'What is the capital of Austria?',
        'answer': 'Vienna'
    }
}

gained_points = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('The answer is: ')

    if answer.lower().strip() == value['answer'].lower():
        print('⭐ Correct ⭐\n')
        gained_points += 1

    else:
        print('Wrong answer!')
        print(f'The answer is: {value["answer"]}\n')

print(f'Your score is: {gained_points} from 7 questions total.\n')
