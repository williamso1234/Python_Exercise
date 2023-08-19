class Critter(object):
    """ The virtual pet """

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        line = 'Critter object\n'
        line += "Name: '" + self.name + "'\n"
        line += 'Hunger level: ' + str(self.hunger) + '\n'
        line += 'Boredom level: ' + str(self.boredom) + '\n'
        line += 'Total unhappiness level: ' + str(self.boredom + self.hunger) + '\n'
        return line

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = 'happy'
        elif 11 <= unhappiness <= 15:
            m = 'frustrated'
        else:
            m = 'mad'
        return m

    def talk(self):
        print('I\'m', self.name, 'and I feel', self.mood, 'now.\n')
        self.__pass_time()

    def eat(self, food=4):
        print('\'eating\'')
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=4):
        print('\'playing\'')
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input('What do you want to name your critter> :')
    crit = Critter(crit_name)
    choice = None
    while choice != '0':
        print(
            '''
            Critter Care

            0 - Quit
            1 - Listen to your critter
            2 - Feed your critter
            3 - Play with your critter
            '''
        )
        choice = input('Choice> :')

        if choice == '0':
            print('Bye')
        elif choice == '1':
            crit.talk()
            print(crit)
        elif choice == '2':
            food = int(input('How many pounds of food would you like to feed your critter> :'))
            while not (6 > food > 0):
                print('Error... Try Again')
                food = int(input('How many pounds of food would you like to feed your critter (1, 5)> :'))
            crit.eat()
            print(crit)
        elif choice == '3':
            play = int(input('How many minutes would you like to play with your critter> :'))
            while not (6 > play > 0):
                print('Error... Try Again')
                play = int(input('How many minutes would you like to play with your critter (1, 5)> :'))

            crit.play()
            print(crit)
        else:
            print('\nError... Try again..')


main()
