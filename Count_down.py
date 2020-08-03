import time
import sys

def count():
    time_in = input('Input the time(HH:MM:SS): ')  # ask for a input
    time_store = time_in.split(':')
    for t in range(3):
        time_store[t] = int(time_store[t])  # changing element in list to int for cal purpose
        if t != 0 and time_store[t] >= 60:  # auto correct the input error if min or sec > 60
            time_store[t] -= 60
            time_store[t - 1] += 1
    total_sec = ((time_store[0] * 60 + time_store[1]) * 60) + time_store[2] # calculate the total sec
    for sec in range(total_sec):
        for t in range(3):
            time_store[t] = str(time_store[t]).zfill(2)  # fill in with zero if needed
        width = int(sec / total_sec * 50)  # creating total width for progress bar
        sys.stdout.write('{}:{}:{}    ['.format(time_store[0], time_store[1], time_store[2]) + '=' * width + ' ' * (49 - width) + ']' + '\r')  # constructing timer and progress bar
        sys.stdout.flush()
        time.sleep(1)
        for t in range(3):
            time_store[t] = int(time_store[t])
        if time_store[2] == 00 and time_store[1] != 00:  # converting min and sec
            time_store[1] -= 1
            time_store[2] = 60
        if time_store[1] == 00 and time_store[0] != 00:
            time_store[0] -= 1
            time_store[1] = 60
        time_store[2] -= 1

count()
print("Time's up")