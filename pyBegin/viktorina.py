from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Викторина")
root.geometry("400x400")


def que_one():
    question = Label(root, text="visit grusha nizia scusat")
    answer = Entry()
    btn = Button(root, text="otvetit", command=lambda: game1(que_two))
    question.grid()
    answer.grid()
    btn.grid()

    def game1(que_two):
        if answer.get().lower() == "lamp":
            que_two()
        else:
            messagebox.showerror("error", "try one more time")


def que_two():
    question_2 = Label(root, text="zimoi i letom kladem plitku")
    answer_2 = Entry()
    btn_2 = Button(root, text="otvetit", command = lambda: game2(que_two))
    question_2.grid()
    answer_2.grid()
    btn_2.grid ()

    def game2(que_two):
        if answer_2.get().lower() == "ell":
            messagebox.showinfo("win!")
        else:
            messagebox.showerror("error", "try again")

que_one()

root.mainloop()
