import random

print('\t\tGuess My Number')
print('Guess a number 1 to 100')

number = random.randint(1, 100)

tries = 0

while True:
    try:
        guess = int(input('Take a guess: '))
        if guess < 1 or guess > 100:
            print('Please enter a number between 1 and 100.')
            continue
        break
    except ValueError:
        print('Invalid input. Please enter a valid integer.')

while guess != number:
    if guess > number:
        print('Lower..')
    else:
        print('Higher..')

    tries += 1

    while True:
        try:
            guess = int(input('Take a guess: '))

            def ask_number(question, low, high):
                response = None
                while response not in range(low, high):
                    response = int(input(question))
                return response

            break
        except ValueError:
            print('Invalid input. Please enter a valid integer.')

tries += 1

print('You guessed it!')
print('It took you', tries, 'tries.')

