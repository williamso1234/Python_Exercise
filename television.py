class Television(object):
    """ The virtual television """

    def __init__(self, channel, volume):
        self.channel = channel
        print('Channel:' + str(self.channel) + '\n')
        self.volume = volume
        print('Volume:' + str(self.volume) + '\n')

    def change_chan(self, c_c):
        self.channel = c_c
        print('Channel:' + str(self.channel))
        print('Volume:' + str(self.volume) + '\n')

    def change_vol(self, vol_up_down):
        if vol_up_down == '1':
            if self.volume < 10:
                self.volume += 1
                print('Volume at:' + str(self.volume))
            elif self.volume == 10:
                print('Maximum Volume')
        elif vol_up_down == '2':
            if self.volume > 0:
                self.volume -= 1
                print('Volume at:' + str(self.volume))
            elif self.volume == 0:
                print('Lowest Volume')
        print('Channel:' + str(self.channel))
        print('Volume:' + str(self.volume) + '\n')


def main():
    channel = 1  # Initial channel
    volume = 5  # Initial volume
    television = Television(channel, volume)

    while True:
        print('''
        Remote Choices. 

        0: Quit
        1: Change Channel
        2: Change Volume
        ''')
        choice = input('Choice: ')

        if choice == '0':
            print('Bye')
            break
        elif choice == '1':
            while True:
                channel_choice = input('What channel (1-10)> : ')
                channel_choice = int(channel_choice)
                if 1 <= channel_choice and channel_choice <= 10:
                    choice_channel = int(channel_choice)
                    television.change_chan(choice_channel)
                    break
                else:
                    print('This channel doesn\'t exist... Try Again')

        elif choice == '2':
            up_down = input('Type "1" for (down) and "2" for (up): ')
            while True:
                if up_down == '1' or up_down == '2':
                    television.change_vol(up_down)
                    break
                else:
                    print('Error... Try again.')
                    up_down = input('Type "1" for (up) and "2" for (down): ')

main()


