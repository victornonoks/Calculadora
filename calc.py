from tkinter import *

app = Tk()

show = ""  # Variavel que vai mudar o texto.

equation = StringVar() # Variavel que vai mostrar o texto.

display = Label(app, textvariable = equation, font=20) # Labelpara o display do texto.

equation.set("") # Texto inicial no display.

display.grid(columnspan = 4) # Expandir o display em 4 espaços no grid.


# Função que adiciona o valor do botao pressionado ao display.
def btnPress(num):  
    global show
    show = show + str(num)
    equation.set(show)

# Função que faz o calculo da equação.
def evaluate():
    global show
    total = str(eval(show))
    equation.set(total)
    show= ""

# Função que limpa o display.
def clear():
    global show
    show = ""
    equation.set(show)

# Função que cria os botões.
def createBtn(master, textBtn, cmd):
    btn = Button(master, text=textBtn, width=5, height=2, font=20, command = lambda:btnPress(cmd))
    return btn

# botoes numericos.
one = createBtn(app, '1', 1)
one.grid(row = 1, column = 0)

two = createBtn(app, '2', 2)
two.grid(row = 1, column = 1)

three = createBtn(app, '3', 3)
three.grid(row = 1, column = 2)

four = createBtn(app, '4', 4)
four.grid(row = 2, column = 0)

five = createBtn(app, '5', 5)
five.grid(row= 2, column = 1)

six = createBtn(app, '6', 6)
six.grid(row = 2, column = 2)

seven = createBtn(app, '7', 7)
seven.grid(row = 3, column = 0)

eight = createBtn(app, '8', 8)
eight.grid(row = 3, column = 1)

nine = createBtn(app, '9', 9)
nine.grid(row = 3, column = 2)

zero = createBtn(app, '0', 0)
zero.grid(row = 4, column = 1)

# Botoes de operadores.

plus = createBtn(app, '+', "+")
plus.grid(row = 1, column = 3)

minus = createBtn(app, '-', "-")
minus.grid(row = 2, column = 3)

div = createBtn(app, '/', "/")
div.grid(row = 3, column = 3)

mult = createBtn(app, 'x', "*")
mult.grid(row = 4, column = 3)

# Finalizador da conta
equal = Button(app, text = "=", width=5, height=2, font=20, command =  evaluate)
equal.grid(row = 4, column = 2)

# Limpa o display
clear = Button(app, text = "C", width=5, height=2, font=20, command = clear)
clear.grid(row= 4, column = 0)

app.mainloop()