from tkinter import *
from tkinter.messagebox import *

win = Tk()
win.title("Calculator")
win.resizable(width=False, height=False)


def main(key):
    if key in "0123456789+-/*.()":
        entry.insert(END, key)
    elif key == "C":
        entry.delete(0, END)
    elif key == "←":
        entry.delete(len(entry.get())-1)  # стираем последний символ в поле ввода
    elif key == "x²":
        entry.insert(END, "**(2)")
    elif key == "x³":
        entry.insert(END, "**(3)")
    elif key == "√":
        entry.insert(END, "**(0.5)")
    elif key == "=":
        try:
            res = eval(entry.get())
            entry.insert(END, "=" + str(res))
        except SyntaxError:
            showerror("Error", "Syntax error!")
        except NameError:
            showerror("Error", "Input error!")
        except ZeroDivisionError:
            showerror("Error", "Division by zero!")


def color(number):
    if number == 1:
        win.config(bg="white")
        for i in range(len(btns)):
            btns[i].config(bg="white", fg="black")
    elif number == 2:
        win.config(bg="gray")
        for i in range(len(btns)):
            btns[i].config(bg="black", fg="white")
    elif number == 3:
        win.config(bg="lightpink")
        for i in range(len(btns)):
            btns[i].config(bg="pink", fg="white")


def theme():
    win1 = Tk()
    win1.title("Themes")
    win.resizable(width=False, height=False)

    Label(win1, text="Colours").grid(row=0, column=0)
    color = StringVar()
    r1 = Radiobutton(win1, text="Светлая", variable=color, value="light", command=lambda x=1: color(x))
    r1.grid(row=1, column=0, sticky=W)
    r1.select()


def size():
    pass


def about():
    showinfo("About the program...", "Писала долго, но справилась :) Апрель 2020, Ялта")

def exit():
    win.destroy()

# главное меню
mainmenu = Menu(win)
win.config(menu=mainmenu)

# первое подменю
menu1 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="Settings", menu=menu1)
# команды первого подменю
menu1.add_command(label="Theme", command=theme)
menu1.add_separator()
menu1.add_command(label="Font size", command=size)

# второе подменю
menu2 = Menu(mainmenu, tearoff=0)
mainmenu.add_cascade(label="About the program", command=about)

# комманда в главном меню
mainmenu.add_command(label="Exit", command=exit)

# создание поля ввода
entry = Entry(width=60, bd=3, relief=SUNKEN)
entry.grid(row=0, columnspan=8)

# надписи на кнопках
btns_text = ["1", "2", "3", "4", "+", "-", "←", "C",
             "5", "6", "7", "8", "*", "/", ".", "√",
             "9", "0", "(", ")", "=", "x²", "x³", "❤"]
# список кнопок (виджетов)
btns = []
r = 1
c = 0
for i in btns_text:
    # размещение очередной кнопки в окне
    btn = Button(win, text=i, width=8, bd=4, command=lambda x=i: main(x))
    btn.grid(row=r, column=c, padx=1, pady=1)
    # добавление созданной кнопки (btn) в список кнопок (buttons)
    btns.append(btn)
    # подготовимся к выводу следующей кнопки
    c += 1
    if c > 7:
        c = 0
        r += 1


win.mainloop()
