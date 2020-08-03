# program for  discord gambling bot

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
# input information
gmail = input('Input your email: ')
password = input('Input your password')
discord = input('link to your channel: ')
channel_no = input('Channel number: ')
print('loading page')
driver = webdriver.Chrome(executable_path='./chromedriver')
driver.get(discord)



class gamble:
    def __init__(self, credit):
        self.input_box = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/div/div[2]/div[2]/div/main/form/div/div/div/div/div[3]/div[2]')
        self.credit = int(credit)
        self.direct = 50
        self.win = 0
        self.lose = 0
        self.exp = 0

    def search(self):
        if int(self.credit) < 25:
            self.input_box.send_keys('+search')  # search for
            self.input_box.send_keys(Keys.ENTER)
            time.sleep(1)
            while True:
                try:
                    message = driver.find_element_by_xpath('//*[@id="messages-50"]/div[2]/div/div/div[2]/div/div[2]').text  # obtaining result message
                    break
                except:
                    try:
                        message = driver.find_element_by_xpath(
                            '//*[@id="messages-49"]/div[2]/div/div/div[2]/div/div[2]').text
                        break
                    except:
                        try:
                            message = driver.find_element_by_xpath(
                                '//*[@id="messages-51"]/div[2]/div/div/div[2]/div/div[2]').text
                            break
                        except:
                            continue
            message = message.split()
            credit_d = message[2]
            self.credit += int(credit_d)
            print('Current credit:{}'.format(self.credit))
        time.sleep(5)
        self.highlow()

    def highlow(self):
        while True:
            self.input_box.send_keys('+highlow allin')
            self.input_box.send_keys(Keys.ENTER)
            time.sleep(5)
            self.input_box.send_keys('+low')
            self.input_box.send_keys(Keys.ENTER)
            time.sleep(5)
            while True:
                try:  # obtaining result message
                    con = driver.find_element_by_xpath(
                        '//*[@id="messages-49"]/div[2]/div/div/div[3]/div[1]/div[1]').text
                    break
                except:
                    try:
                        con = driver.find_element_by_xpath(
                            '//*[@id="messages-50"]/div[2]/div/div/div[3]/div[1]/div[1]').text
                        break
                    except:
                        try:
                            con = driver.find_element_by_xpath(
                                '//*[@id="messages-51"]/div[2]/div/div/div[3]/div[1]/div[1]').text
                            break
                        except:
                            continue
            if con == 'Incorrect!':  # if result is low
                self.credit = 0
                self.lose += 1
                if int(self.credit) >= 100:
                    while True:
                        try:
                            message = driver.find_element_by_xpath(
                                '//*[@id="messages-49"]/div[2]/div/div/div[4]/span').text
                            break
                        except:
                            try:
                                message = driver.find_element_by_xpath(
                                    '//*[@id="messages-50"]/div[2]/div/div/div[4]/span').text
                                break
                            except:
                                try:
                                    message = driver.find_element_by_xpath(
                                        '//*[@id="messages-51"]/div[2]/div/div/div[4]/span').text
                                    break
                                except:
                                    continue
                    message = message.split()
                    self.exp += int(message[2])
                print('Total win:{}, Total lose:{}, exp gained:{}'.format(self.win, self.lose, self.exp))
                self.search()
            elif con == 'Correct!':  # if result is win
                self.input_box.send_keys('+stop')
                self.input_box.send_keys(Keys.ENTER)
                time.sleep(2)
                if int(self.credit) >= 100:
                    while True:
                        try:
                            message = driver.find_element_by_xpath(
                                '//*[@id="messages-49"]/div[2]/div/div/div[4]/span').text
                            break
                        except:
                            try:
                                message = driver.find_element_by_xpath(
                                    '//*[@id="messages-50"]/div[2]/div/div/div[4]/span').text
                                break
                            except:
                                try:
                                    message = driver.find_element_by_xpath(
                                        '//*[@id="messages-51"]/div[2]/div/div/div[4]/span').text
                                    break
                                except:
                                    continue
                    message = message.split()
                    self.exp += int(message[2])
                self.credit += self.credit
                self.win += 1
                time.sleep(2)
                print('Total win:{}, Total lose:{}, exp gained:{}'.format(self.win, self.lose, self.exp))
                self.highlow()






time.sleep(6)
email = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[1]/div/input')  # getting in the channel
email.send_keys(gmail)
password = driver.find_element_by_xpath('//*[@id="app-mount"]/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/div[2]/div/input')
password.send_keys(password)
login_b = driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div/form/div/div/div[1]/div[3]/button[2]')
login_b.click()
time.sleep(6)
channel = driver.find_element_by_xpath('//*[@id="channels-{}"]/div'.format(channel_no))
channel.click()
user = gamble(input('Input your credit amount: '))
user.search()
