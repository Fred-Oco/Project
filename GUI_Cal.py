from tkinter import *

background = Tk()   # setting up gui
background.title('My calculator')
background.iconbitmap('1200px-Math.svg.png')

input_box = Entry(background, width=45, borderwidth=5, bg='black', fg='white')  # setting and config
input_box.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def cal_process(equation):  # calculation process
    if len(equation) % 2 == 0 or '' in equation:
        return 'Error'
    else:
        while '*' in equation:
            index_val = equation.index('*')
            ans = float(equation[index_val - 1]) * float(equation[index_val + 1])
            equation[index_val] = ans
            del equation[index_val + 1], equation[index_val - 1]
        while '/' in equation:
            index_val = equation.index('/')
            ans = float(equation[index_val - 1]) / float(equation[index_val + 1])
            equation[index_val] = ans
            del equation[index_val + 1], equation[index_val - 1]
        while '+' in equation:
            index_val = equation.index('+')
            ans = float(equation[index_val - 1]) + float(equation[index_val + 1])
            equation[index_val] = ans
            del equation[index_val + 1], equation[index_val - 1]
        while '-' in equation:
            index_val = equation.index('-')
            ans = float(equation[index_val - 1]) - float(equation[index_val + 1])
            equation[index_val] = ans
            del equation[index_val + 1], equation[index_val - 1]
        return equation[0]

def input_num(num):
    current = input_box.get()
    input_box.insert(len(current), num)


def input_func(num):
    current = input_box.get()
    input_box.insert(len(current), num)


def clear():
    current = input_box.get()
    input_box.delete(0, len(current))


def input_equal():
    equation = input_box.get()
    answer = calculate(equation)
    input_box.delete(0, len(equation))
    input_box.insert(0, answer)


def calculate(equation):
    num_list = []
    num_store = ''
    for count in equation:
        if count == '+' or count == '-' or count == '/' or count == '*':
            num_list.append(num_store)
            num_list.append(count)
            num_store = ''
        else:
            num_store += count
    num_list.append(num_store)
    print(num_list)
    return cal_process(num_list)


def delete():
    current = input_box.get()
    input_box.delete(len(current) - 1)

# Define Button


button_1 = Button(background, text='1', padx=40, pady=20, command=lambda: input_num(1))
button_2 = Button(background, text='2', padx=40, pady=20, command=lambda: input_num(2))
button_3 = Button(background, text='3', padx=40, pady=20, command=lambda: input_num(3))
button_4 = Button(background, text='4', padx=40, pady=20, command=lambda: input_num(4))
button_5 = Button(background, text='5', padx=40, pady=20, command=lambda: input_num(5))
button_6 = Button(background, text='6', padx=40, pady=20, command=lambda: input_num(6))
button_7 = Button(background, text='7', padx=40, pady=20, command=lambda: input_num(7))
button_8 = Button(background, text='8', padx=40, pady=20, command=lambda: input_num(8))
button_9 = Button(background, text='9', padx=40, pady=20, command=lambda: input_num(9))
button_0 = Button(background, text='0', padx=40, pady=20, command=lambda: input_num(0))
button_float = Button(background, text='.', padx=41, pady=20, command=lambda: input_func('.'))
button_add = Button(background, text='+', padx=41, pady=20, command=lambda: input_func('+'))
button_minus = Button(background, text='-', padx=42, pady=20, command=lambda: input_func('-'))
button_sub = Button(background, text='*', padx=42, pady=20, command=lambda: input_func('*'))
button_time = Button(background, text='/', padx=42, pady=20, command=lambda: input_func('/'))
button_equal = Button(background, text='=', padx=91, pady=20, command=input_equal)
button_clear = Button(background, text='AC', padx=38, pady=20, command=clear, width=2)
button_del = Button(background, text='Del', padx=40, pady=20, command=delete)

# Put in on screen
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_add.grid(row=1, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_minus.grid(row=2, column=3)

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_time.grid(row=3, column=3)

button_0.grid(row=4, column=0)
button_float.grid(row=4, column=1)
button_clear.grid(row=4, column=2)
button_sub.grid(row=4, column=3)

button_equal.grid(row=5, column=0, columnspan=3)
button_del.grid(row=5, column=3)

background.mainloop()
