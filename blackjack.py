import random

class gamble:

    def __init__(self, money, chip):
        self.chip = int(chip)
        self.money = int(money)
        self.player_total = 0
        self.admin_total = 0
        self.player_card = []
        self.admin_card = []

    def start(self):
        check = False
        while check is False:
            self.player_card.append(random.randint(1, 14))
            self.player_card.append(random.randint(1, 14))
            for number in self.player_card:
                self.player_total += number
            if self.player_total <= 21:
                check = True
        print('The card you have: {}. Total is {}'.format(self.player_card, self.player_total))
        self.admin_card.append(random.randint(1, 14))
        self.admin_card.append(random.randint(1, 14))
        for number in self.admin_card:
            self.admin_total += number
        print('The card admin have: {} *'.format(self.admin_card[0]))
        self.player_option()

    def player_option(self):
        option = input('What is your move?(add or surrender or leave it blank): ')
        if option == 'add':
            self.chip += 20
            self.add_option()
        elif option == 'surrender':
            print('You Lose')
            self.money -= self.chip
            print('You have ${} left'.format(self.money))
            self.restart()
        else:
            self.add_option()

    def add_option(self):
        add = input('Add or Stop?: ')
        if add.strip().title() == 'Add':
            self.player_card.append(random.randint(1, 14))
            self.player_total += self.player_card[len(self.player_card) - 1]
            print('The card you have: {}. Total is {}'.format(self.player_card, self.player_total))
            if self.player_total > 21:
                print('You Lose')
                self.money -= self.chip
                print('You have ${} left'.format(self.money))
                self.restart()
            else:
                self.add_option()
        elif add.strip().title() == 'Stop':
            while self.admin_total < 17:
                self.admin_card.append(random.randint(1, 14))
                self.admin_total += self.admin_card[len(self.admin_card) - 1]
            if self.admin_total > 21:
                print('You Win.Admin busted with {} score'.format(self.admin_total))
                self.money += self.chip
                print('You have ${} left'.format(self.money))
            elif self.admin_total < self.player_total:
                print('You Win.Your score: {},Admin score: {}'.format(self.player_total, self.admin_total))
                self.money += self.chip
                print('You have ${} left'.format(self.money))
                self.restart()
            else:
                print('You Lose.Your score: {},Admin score: {}'.format(self.player_total, self.admin_total))
                self.restart()
        else:
            print('Invalid Input')
            self.add_option()

    def restart(self):
        re = input('Restart(yes or no)? ')
        if re.strip().title() == 'Yes':
            user = gamble(self.money, input('How much you in? '))
            user.start()
        elif re.strip().title() == 'No':
            quit()


User = gamble(input('How much money you have? '), input('How much you in? '))
User.start()

