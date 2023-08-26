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
    crit_name2 = input('What do you want to name your second critter> :')
    crit_name3 = input('What do you want to name your third critter> :')
    crit = Critter(crit_name)
    crit2 = Critter(crit_name2)
    crit3 = Critter(crit_name3)

    choice = None
    while choice != '0':
        print(
            '''
            Critter Care

            0 - Quit
            1 - Listen to your critters     
            2 - Feed your critters
            3 - Play with your critters
            '''
        )
        choice = input('Choice> :')

        if choice == '0':
            print('Bye')
        elif choice == '1':
            print(crit)
            crit.talk()
            print(crit2)
            crit2.talk()
            print(crit3)
            crit3.talk()

        elif choice == '2':
            while True:
                try:
                    pounds_of_food = int(input('How many pounds of food would you like to feed your critters (1-5)> '))
                    if pounds_of_food in [1, 2, 3, 4, 5]:
                        break
                    else:
                        print('Error... Try Again')
                except ValueError:
                    print('Error... Try Again')
            crit.eat()
            crit2.eat()
            crit3.eat()
            print(crit)
        elif choice == '3':
            while True:
                try:
                    play_time = int(input('How many minutes would you like to play with your critters (1-5)> :'))
                    if play_time in [1, 2, 3, 4, 5]:
                        break
                    else:
                        print('Error... Try Again')
                except ValueError:
                    print('Error... Try Again')
            crit.play()
            crit2.play()
            crit3.play()

            print(crit)
        else:
            print('\nError... Try again..')


main()

