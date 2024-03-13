from tkinter import *
from tkinter import ttk

# cores
cor1 = "#030303"  # preto
cor2 = "#7099b8"  # azul
cor3 = '#fad902'  # amarelo
cor4 = '#dbdbd9'  # cinza
cor5 = '#f7f7f7'  # branco

# Janela
janela = Tk()
janela.title("Calculadora")
janela.geometry("300x330")
janela.config(bg=cor1)

# variavel todos_valores
todos_valores = ''
valor_texto = StringVar()

#função adicionar valores
def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    # passando os valores para tela
    valor_texto.set(todos_valores)

# função calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))

# função limpar
def limpar():
    global todos_valores
    todos_valores = ''
    valor_texto.set('')




# Tela
frame_tela = Frame(janela, width=400, height=70, bg=cor2)
frame_tela.grid(row=0, column=0)

# Corpo
frame_corpo = Frame(janela, width=400, height=500)
frame_corpo.grid(row=1, column=0)

# Display
label = Label(frame_tela, textvariable=valor_texto, width=16, height=2, padx=5, relief=FLAT, anchor='e', justify=RIGHT,font=('Yvi 22 bold'), bg=cor1, fg=cor3)
label.place(x=0, y=0)

# primeira fileira
Cancelar = Button(frame_corpo, command=limpar, text="C", width=13, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
Cancelar.place(x=0, y=0)

porcentagem = Button(frame_corpo, command= lambda:entrar_valores('%'), text="%", width=7, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
porcentagem.place(x=140, y=0)

divisao = Button(frame_corpo, command= lambda:entrar_valores('/'), text="/", width=7, height=2, bg=cor3, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
divisao.place(x=220, y=0)

# Segunda fileira
b_x = Button(frame_corpo, command= lambda:entrar_valores('*'), text="*", width=7, height=2, bg=cor3, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_x.place(x=220, y=52)

n_7 = Button(frame_corpo, command= lambda:entrar_valores('7'), text="7", width=6, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_7.place(x=0, y=52)
n_8 = Button(frame_corpo, command= lambda:entrar_valores('8'), text="8", width=6, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_8.place(x=70, y=52)
n_9 = Button(frame_corpo, command= lambda:entrar_valores('9'), text="9", width=7, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_9.place(x=140, y=52)

# Terceira fileira
b_menos = Button(frame_corpo, command= lambda:entrar_valores('-'), text="-", width=7, height=2, bg=cor3, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_menos.place(x=220, y=104)

n_4 = Button(frame_corpo, command= lambda:entrar_valores('4'), text="4", width=6, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_4.place(x=0, y=104)
n_5 = Button(frame_corpo, command= lambda:entrar_valores('5'), text="5", width=6, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_5.place(x=70, y=104)
n_6 = Button(frame_corpo, command= lambda:entrar_valores('6'), text="6", width=7, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_6.place(x=140, y=104)

# Quarta fileira
b_mais = Button(frame_corpo, command= lambda:entrar_valores('+'), text="+", width=7, height=2, bg=cor3, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_mais.place(x=220, y=156)

n_1 = Button(frame_corpo, command= lambda:entrar_valores('1'), text="1", width=6, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_1.place(x=0, y=156)
n_2 = Button(frame_corpo, command= lambda:entrar_valores('2'), text="2", width=6, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_2.place(x=70, y=156)
n_3 = Button(frame_corpo, command= lambda:entrar_valores('3'), text="3", width=7, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
n_3.place(x=140, y=156)

# Quinta fileira
b_igual = Button(frame_corpo, command = calcular, text="=", width=7, height=2, bg=cor3, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_igual.place(x=220, y=208)
b_0 = Button(frame_corpo, command= lambda:entrar_valores('0'), text="0", width=13, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_0.place(x=0, y=208)
b_ponto = Button(frame_corpo, command= lambda:entrar_valores('.'), text=".", width=7, height=2, bg=cor4, font=('Yvi 13 bold'), relief=RAISED, overrelief=RIDGE)
b_ponto.place(x=140, y=208)


janela.mainloop()
