#imports

from tkinter import *
from tkinter.ttk import *

#defs

#screen build

screen = Tk()
screen.geometry("600x600")
screen.title("pizza")
screen.config(background = "gray")

#defs

def confirm():
    name = type.get()
    quantity = amount.get()
    width = size.get()

    rec = "your order is: " + name + ", " + quantity + ", " + width
    order.config(text = rec)

#widgets

welcome = Label(screen,text = "welcome to pizza hut", background = "gray", foreground = "maroon", font = ("times", "50" ))
welcome.place(x = 150, y = 100)

select_p = Label(screen,text = "select your pizza:", background =  "gray", foreground = "maroon", font = ("times", "30" ))
select_p.place(x = 100, y = 300)

select_q = Label(screen,text = "select the quantity:", background = "gray", foreground = "maroon", font = ("times", "30" ))
select_q.place(x = 100, y = 400)

order = Label(screen, text =  "" , background = "gray", foreground = "maroon", font = ("times", "25"))
order.place(x = 100, y = 500)

done = Button(screen, text = "finish order", command = confirm)
done.place(x = 300, y = 450)

#combobox

type = StringVar()
amount = StringVar()
pizza_selections = Combobox(screen, textvariable = type, width = 10)
pizza_selections['values'] = ['pepperoni','vegan','americano','cheese','salami','vegtable','hawaii','persian style','margarita','mushroom']
pizza_selections.place(x = 350, y = 300)
pizza_amount = Combobox(screen, textvariable = amount, width = 5)
pizza_amount['values'] = ['1','2','3','4','5','6','7','8','9','10']
pizza_amount.place(x = 350, y = 400)

#radiobutton

size = StringVar()

small = Radiobutton(screen,text = "S", variable = size, value = "S")
small.place(x = 500, y = 300)
medium = Radiobutton(screen,text = "M", variable = size, value = "M")
medium.place(x = 500, y = 350)
large = Radiobutton(screen,text = "L", variable = size, value = "L")
large.place(x = 500, y = 400)

#finish ups
screen.mainloop()
