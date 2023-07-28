import sys


def open_file(file_name, mode):
    """ OPEN FILE """
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print('Unable to open the file', file_name, 'Ending program.\n', e)
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """ Return next line from the trivia file """
    line = the_file.readline()
    line = line.replace('/', '\n')
    return line


def next_block(the_file):
    """ Return the next block of data from the trivia file. """
    category = next_line(the_file)

    question = next_line(the_file)

    answers = []
    for i in range(4):
        answers.append(next_line(the_file))

    correct = next_line(the_file)
    if correct:
        correct = correct[0]

    explanation = next_line(the_file)
    value = next_line(the_file)
    try:
        value = int(value)
    except ValueError:
        if category:
            pass
    return category, question, answers, correct, explanation


def welcome(title):
    """ Welcome the player and get name """
    print('\t\tTrivia')
    print('\t\t', title, '\n')


def main():
    trivia_file = open_file('trivia.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # get first block
    category, question, answers, correct, explanation, = next_block(trivia_file)
    while category:
        # ask a question
        print(category)
        print(question)
        for i in range(4):
            print('\t', i + 1, '-', answers[i])
        # get answer
        answer = input('What\'s your answer? : ')
        # check answer
        if answer == correct:
            print('\nCorrect', end=' ')
            score += 1
        else:
            print('\nIncorrect', end=' ')
        print(explanation)
        print('Score:', score, '\n\n')
        # get next block
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print('That was the last question')
    print('Your final score is', score)


main()
