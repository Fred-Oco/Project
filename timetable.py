import datetime
# set up list for different day
day1_list = ['Assembly', 'English', 'English', 'Recess', 'Chinese', 'Biology', 'Biology', 'Lunch', 'BAFS', 'BAFS',
             'Mathematics']
day2_list = ['English', 'English', 'Chinese', 'Recess', 'Mathematics', 'Chinese History', 'Chinese History', 'Lunch',
             'Biology', 'IES', 'IES']
day3_list = ['Chinese', 'Chinese History', 'Chinese History', 'Recess', 'BAFS', 'BAFS', 'Biology', 'Lunch',
             'Mathematics', 'English', 'English']
day4_list = ['Assembly', 'LS', 'LS', 'Recess', 'Mathematics', 'English', 'English', 'Lunch', 'Chinese History',
             'Chinese', 'Chinese']
day5_list = ['Ethic', 'Biology', 'Biology', 'Recess', 'Chinese', 'Chinese', 'BAFS', 'Lunch', 'English', 'English',
             'Mathematics']
day6_list = ['Mathematics', 'Mathematics', 'Chinese', 'Recess', 'Chinese History', 'LS', 'LS', 'Lunch', 'BAFS',
             'PE', 'PE']
# starting time of each lesson
start_time = [['08', '35'], ['09', '10'], ['09', '45'], ['10', '20'], ['10', '40'], ['11', '15'], ['11', '50'],
              ['12', '25'], ['13', '45'], ['14', '20'], ['14', '55'], ['15', '30']]

all_list = [day1_list, day2_list, day3_list, day4_list, day5_list, day6_list]
today_list = []


class timetable:
    def __init__(self, day):
        self.day = day
        self.today_list = all_list[int(self.day) - 1]
        self.index = 0
        self.hour = self.GetTime_H()
        self.min = self.GetTime_M()

    def GetTime_H(self):  # get current time in Hour
        now_time = datetime.datetime.now()
        return now_time.strftime('%H')

    def GetTime_M(self):  # get current time in Min
        now_time = datetime.datetime.now()
        return now_time.strftime('%M')

    def Check_pre(self):  # give out correct respond according to checking result
        if self.before_after_sku_check() is True:
            print('Not yet school yet')
        elif self.same_time_check() is True:
            print('It is the end of {}.Starting of {}.'.format(self.today_list[self.index - 1], self.today_list[self.index]))
        elif self.inbetween_lesson_check() is True:
            remain_time = self.remain_time()
            if self.index == 4 or self.index == 8 or self.index == 1:  # including recces time
                print('You are currently in {} period, approx. {} min left from {}'.format(
                    self.today_list[self.index - 1], remain_time, self.today_list[self.index]))
            else:
                print('You are currently in {} lesson, approx. {} min left from {}'.format(self.today_list[self.index - 1], remain_time, self.today_list[self.index]))
        else:
            remain_time = 30 - int(self.min)
            print('You are currently in {} lesson, approx. {} min left from leaving school'.format(self.today_list[self.index - 1], remain_time))
        self.print_tabel()

    def remain_time(self):  # calculate the time difference
        if int(self.hour) == int(start_time[self.index][0]):
            remain = int(start_time[self.index][1]) - int(self.min)
        else:
            remain = int(start_time[self.index][1]) + 60 - int(self.min)
        return remain

    def before_after_sku_check(self):  # checking time for scenario of before or after school time
        if start_time[0][0] == self.hour and start_time[0][1] >= self.min:
            return True
        elif start_time[0][0] > self.hour:
            return True
        elif start_time[11][0] == self.hour and start_time[11][1] <= self.min:
            return True
        elif start_time[11][0] < self.hour:
            return True
        else:
            return False

    def same_time_check(self):  # including scenario which current time is at the starting time
        for num in range(len(self.today_list)):
            if start_time[num][0] == self.hour and start_time[num][1] == self.min:
                self.index = num
                return True
        return False

    def inbetween_lesson_check(self):  # check if current time is in-between lesson
        for num in range(11):
            if start_time[num][0] == self.hour and start_time[num][1] > self.min:
                self.index = num
                return True
            elif start_time[num][0] > self.hour:
                self.index = num
                return True

    def print_tabel(self):  # print out time table
        print('This is Today timetable: ')
        for num in range(len(self.today_list)):
            time_h = start_time[num][0]
            time_m = start_time[num][1]
            print('{}:{}  {}'.format(time_h, time_m, self.today_list[num]))


user = timetable(input("What is today's day? "))  # asking for user input
user.Check_pre()