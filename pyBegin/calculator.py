from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math

root = Tk()
root.title("калькулятор")

# создание кнопок
bttn_list = [
"MS", "M+", "M-", "MR", "MC",
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3", "=", "C",
"±", "0", ".", "(", ")",
"xⁿ", "n!", "π", "e", "exp",
"√2", "asin", "sin", "cos", "tg",
"log", "log10", "ln", "", ""
 ]

memoryValue = 0
global memory
memory = 0
r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd = lambda x = i: calc(x)
    ttk.Button(root, text = i, command = cmd, width = 10).grid(row = r, column =c)
    c += 1
    if c > 4:
        c = 0
        r += 1

# калькулятор собственной персоны
def calc(key):
    global memory
    if key == "=":
 # исключение написания букв и других сторонних симвлов
        str1 = "-+0123456789.*/)("
        if calc_entry.get()[0] not in str1:
            calc_entry.insert(END, "Первый символ не число")
            messagebox.showerror(("ошибка", "Вы ввели не число!"))
# счет
        try:
            result = eval(calc_entry.get())
            calc_entry.delete(0, END)
            calc_entry.insert(END, str(result))
        except ZeroDivisionError:
            messagebox.showerror("Деление на 0 запрещено!")
        except:
            calc_entry.insert((END, "error!"))
            messagebox.showerror("Вы ввели не число!")
# очистить поле
    elif key == "C":
        calc_entry.delete(0, END)
# замена  +/-
    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get() [0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass
    elif key == "π":
        calc_entry.insert(END, math.pi)
    elif key == "e":
        calc_entry.insert(END, math.e)
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
# trigonomic expresions
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(int(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(int(calc_entry.get()))))
    elif key == "tg":
        calc_entry.insert(END, "=" + str(math.tan(int(calc_entry.get()))))
    elif key == "asin":
        calc_entry.insert(END, "=" + str(math.asin(int(calc_entry.get()))))
# скобки
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
# другие операции
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(int(calc_entry.get()))))
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(int(calc_entry.get()))))
    elif key == "exp":
        calc_entry.insert(END, "=" + str(math.exp(int(calc_entry.get()))))
    elif key == "log":
        calc_entry.insert(END, "=" + str(math.log(int(calc_entry.get()))))
    elif key == "log10":
        calc_entry.insert(END, "=" + str(math.log10(int(calc_entry.get()))))
    elif key == "ln":
        calc_entry.insert(END, "=" + str(math.log1p(int(calc_entry.get()))))
# память
    elif key == "MS" :
        memory = int(calc_entry.get())
    elif key == "M+":
        memory += int(calc_entry.get())
    elif key == "M-":
        memory -=int(calc_entry.get())
    elif key == "MR":
        calc_entry.delete(0, END)
        calc_entry.insert(END, memory)
    elif key == "MC":
        memory = 0
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
            calc_entry.insert(END, key)
        else:
            calc_entry.insert(END, (key))




calc_entry = Entry(root, width = 57)
calc_entry.grid(row = 0, column = 0, columnspan = 10)



root.mainloop()