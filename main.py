from killer import choose_killer
from killer import randomize_killer_perks
from survivor import choose_survivor
from survivor import randomize_survivor_perks
import time

def main():
    print('Welcome to Dbd Perk Roulette.')
    time.sleep(1)
    action = int(input('To draw killer perks, enter: 1. To draw survivor perks, enter 2.\n'))
    if action == 1:
        choose_killer()
        randomize_killer_perks()
        print('Have a good game!')
    elif action == 2:
        choose_survivor()
        randomize_survivor_perks()
        print('Have a good game!')
    else:
        print('Invalid data.')


if __name__ == '__main__':
    main()