import sys
import pickle


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
        value = 1  # Default value

    return category, question, answers, correct, explanation, value


def welcome(title):
    """ Welcome the player """

    print('\t\tTrivia')
    print('\t\t', title, '\n')


def high_scores():
    hs = []
    try:
        with open('high_scores.txt', 'r') as f:
            for line2 in f:
                if ',' not in line2:
                    print('line without ,:', line2)
                    continue
                name, score = line2.strip().split(', ')
                # Remove the many Name:
                name = name.replace("Name: ", "")
                score_value = int(score.split(': ')[1])
                hs.append((name, score_value))
    except FileNotFoundError:
        # The file doesn't exist yet or is empty, so we'll create it when we save the data.
        pass

    name = input('What is your name? : ')
    score = input('What is your score? : ')
    entry = (name, int(score))
    hs.append(entry)

    def sort_by_score(entry):
        return entry[1]

    # Sort the high scores list backwards
    hs.sort(key=sort_by_score, reverse=True)

    # Keep only the top 3 high scores
    hs = hs[:3]

    # Write the updated high scores back to the file
    with open('high_scores.txt', 'w') as f:
        for name, score in hs:
            f.write(f'Name: {name}, Score: {score}\n')


def main():
    trivia_file = open_file('trivia.txt', 'r')
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    # get first block
    category, question, answers, correct, explanation, value = next_block(trivia_file)
    while category:
        # ask a question with point value
        print(category)
        print(question)
        for i in range(4):
            print('\t', i + 1, '-', answers[i])
        # get answer
        answer = input('What\'s your answer (1 - 4)? : ')
        # check answer

        if answer == correct:
            print(f'\nCorrect. You earned {value} point\'   .', end=' ')
            score += value
        else:
            print('\nIncorrect.', end=' ')
        print(explanation)
        print('Score:', score, '\n\n')
        # get next block
        category, question, answers, correct, explanation, value = next_block(trivia_file)

    trivia_file.close()

    print('That was the last question')
    print('Your final score is', score)
    high_scores()


main()
