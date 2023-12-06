from tkinter import *
from tkinter import messagebox
import numpy as np
import pandas as pd
import threading
import time

root = Tk()

root['bg'] = 'white'
root.title('Шифр Цезаря')
root.geometry('730x350')

root.resizable(width=False, height=False)



def btn2_click():
    if textInput.get() == '':
        messagebox.showerror(title='Ошибка', message='Введите значение')
        exit()
    e.set()
def btn_click():
    t = threading.Thread(target=func,
                         args=(e,))
    t.start()

def func(e):
    if textInput.get() == '':
        messagebox.showerror(title='Ошибка', message='Введите значение')
        exit()
    num = textInput.get()
    num = int(num)


    error = 0
    textInput.delete(0, END)
    M = np.ones([num, num])  # Создаем матрицу
    btn1.grid_forget()
    btn2 = Button(frame, text='Ввод', bg='white', command=btn2_click, width=5, height=1)
    btn2.grid(row=6, column=1)
    while True:
        for i in range(0, num):
            for j in range(0, num):
                if i < j:
                    #print('\tTHREAD: This is the thread speaking, we are Waiting for event to start..')
                    text2["text"] = f'Насколько критерий {i+1} приоритетнее критерия {j+1}? Введите коэффициент числом: '
                    event_is_set = e.wait()
                    matrixij = textInput.get()
                    if matrixij == '1':
                        error += 1
                    textInput.delete(0, END)
                    M[i, j] = float(matrixij)
                    M[j, i] = 1 / float(matrixij)  # Добавление обратных элементов (под главной диагональю)
                    e.clear()
                    text2["text"] = ''
        break
    btn2.grid_forget()
    textInput.grid_forget()
    text2["text"] = ''
    v = np.linalg.eig(M)[1][:, 0]
    nv = v / v.sum()
    if error == num:
        text3 = Label(frame, text="Ваши критерии равносильны", bg='white')
        text3.grid(row=2, column=1)
    else:
        for x in range(len(nv)):
            res = list(str(nv[x]))
            if res[len(res)-2] == "j":
                ''.join(res)
                res = res[:-4]
                list(res)
                res.pop(0)
            res = float(''.join(res)) // 0.01 / 100
            text = f"Коэффициент критерия {x + 1}: {res}"
            text3 = Label(frame, text=text, bg='white')
            text3.grid(row=2+x, column=1)
    return nv

e = threading.Event()


frame = Frame(root, bg='white')
frame.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.8)

text2 = Label(frame, text="Сколько критериев Вы желаете рассмотреть?", bg='white')
text2.grid(row=2, column=1)

space = Label(frame, text="", bg='white')
space.grid(row=3, column=1)

textInput = Entry(frame, bg='white', width=70)
textInput.grid(row=4, column=1)

space1 = Label(frame, text="", bg='white')
space1.grid(row=5, column=1)

btn1 = Button(frame, text='Ввод', bg='white', command=btn_click, width=5, height=1)
btn1.grid(row=6, column=1)


mainloop()