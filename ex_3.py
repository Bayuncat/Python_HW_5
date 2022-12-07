from tkinter import *
import sys
import os
from tkinter import Tk, Label, Button
from tkinter import ttk

def restart():
    root.destroy()
    os.startfile("test_2.py")

root = Tk()
root.title('Крестики-нолики. V.1.0')
root.geometry('500x500')
btn = ttk.Button(root, text="Сыграть заново", command=restart)
btn.pack(side="top")

games = Canvas(root, width=450, height=450)
games.place(x=60,y=60)

field = [None] * 9
stepList = ['o']
win = None
winCombinatons = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

def checkWin():
    winner = None
    variants = []
    for i in winCombinatons:
        variants.append([field[i[0]], field[i[1]], field[i[2]]])
    if ['x'] * 3 in variants:
        winner = 'Победили Х'
    elif ['o'] * 3 in variants:
        winner = 'Победили О'
    elif None not in field:
        winner = 'Ничья'
    return winner

for i in range(0,9):
    x = i//3 * 120
    y = i%3 * 120
    games.create_rectangle(x, y, x + 120, y + 120,
            width=3,
            outline='#53868B',
            fill='#4a7abc',
            activefill='white')

def add_x(column, row):
    x = 10 + 120*column
    y = 10 +120*row
    games.create_line(x, y, x + 100, y + 100, width=10, fill='black')
    games.create_line(x, y + 100, x + 100, y, width=10, fill='black')

def add_o(column, row):
    x = 10 + 120*column
    y = 10 +120*row
    games.create_oval(x, y, x + 100, y + 100, width=10, outline='black')

def click(event):
    column = event.x // 120
    row = event.y // 120
    index = column + row*3
    
    if ((field[index] is None) and (stepList[-1] == 'o')):
        field[index] = 'x'
        add_x(column, row)
        stepList.append('x')
        if checkWin() == 'Победили Х': 
            print("Игра окончена. Победили Х")

    elif ((field[index] is None) and (stepList[-1] == 'x')):
        field[index] = 'o'
        add_o(column, row)
        stepList.append('o')
        if checkWin() == 'Победили О': print("Игра окончена. Победили O")

    else:
        print(field)
 
games.bind('<Button-1>', click)

root.mainloop()