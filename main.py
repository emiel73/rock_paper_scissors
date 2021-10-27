import sys
from itertools import chain, islice
from random import choice


class Game:
    def __init__(self):
        self.user_name: str = input('Enter your name: ').title()
        self.user_points: int = 0
        self.options: list = ['rock', 'paper', 'scissors']
        self.rules: list = []
        self.stronger: list = []
        self.weaker: list = []
        self.set_user_points()

    def set_user_points(self):
        with open('rating.txt') as file:
            for line in file:
                name = line.strip().split()[0]
                if self.user_name == name:
                    self.user_points = int(line.strip().split()[1])

    def greet_user(self):
        print(f'Hello, {self.user_name}')

    def get_user_options(self):
        user_input = input()
        if user_input:
            user_input = [el.strip() for el in user_input.split(',')]
            if len(user_input) >= 3:
                self.options = user_input
            else:
                print('You have to enter at least 3 options separated by coma.',
                      'Otherwise you are playing traditional version: rock, paper, scissors')

    def get_user_choice(self):
        user_input = input().lower()
        if user_input == '!exit':
            print('Bye!')
            sys.exit()
        elif user_input == '!rating':
            print(f'Your rating: {self.user_points}')
        elif user_input in self.options:
            self.set_rules(user_input)
            self.check_winner(user_input)
        else:
            print('Invalid input')

    def set_rules(self, user_choice):
        self.rules = [element for element in
                      (chain(islice(self.options, self.options.index(user_choice) + 1, None),
                             islice(self.options, self.options.index(user_choice))))]
        self.stronger = self.rules[:int(len(self.rules) / 2)]
        self.weaker = self.rules[int(len(self.rules) / 2):]

    def check_winner(self, player):
        comp = choice(self.options)
        if player == comp:
            print(f'There is a draw ({comp})')
            self.user_points += 50
        elif comp in self.weaker:
            print(f'Well done. The computer chose {comp} and failed')
            self.user_points += 100
        else:
            print(f'Sorry, but the computer chose {comp}')

    def play(self):
        self.greet_user()
        self.get_user_options()
        print("Okay, let's start")
        while True:
            self.get_user_choice()


def main():
    rps = Game()
    rps.play()


if __name__ == '__main__':
    main()
