from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Agenda')
        self.janela.geometry('610x180')
        self.janela.resizable(width = False, height = False)

        self.Label1 = Label(background = 'Black', borderwidth = 2, font = 'Arial 25 bold', foreground = 'White', text = 'Minha Agenda')
        self.Label1.place(x = 5, y = 4, height = 50, width = 497)
        self.Label2 = Label(font = 'Arial 16 bold', text = 'Nome:')
        self.Label2.place(x = 12, y = 72, height = 30, width = 70)
        self.Label3 = Label(font = 'Arial 16 bold', text = 'Telefone:')
        self.Label3.place(x = 6, y = 133, height = 30, width = 111)

        self.Entry1 = Entry(borderwidth = 3, font = 'Arial 16 bold', foreground = 'blue', justify = 'left')
        self.Entry1.place(x = 119, y = 64, height = 47, width = 380)
        self.Entry2 = Entry(borderwidth = 3, font = 'Arial 16 bold', foreground = 'blue', justify = 'left')
        self.Entry2.place(x = 119, y = 122, height = 47, width = 380)

        self.Button1 = Button(background = 'green', font = 'Arial 12 bold', foreground = 'white', text = 'Limpar')
        self.Button1.place(x = 510, y = 4, height = 70, width = 96)
        self.Button2 = Button(background = 'yellow', font = 'Arial 12 bold', text = 'Inserir')
        self.Button2.place(x = 510, y = 80, height = 40, width = 98)
        self.Button3 = Button(background = 'orange', font = 'Arial 12 bold', text = 'Consultar')
        self.Button3.place(x = 510, y = 127, height = 40, width = 99)

        self.janela.mainloop()

aplicacao=App()
