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

        self.Button1 = Button(background = 'green', font = 'Arial 12 bold', foreground = 'white', text = 'Inserir')
        self.Button1.place(x = 510, y = 9, height = 35, width = 96)
        self.Button2 = Button(background = 'yellow', font = 'Arial 12 bold', text = 'Consultar', )
        self.Button2.place(x = 508, y = 57, height = 36, width = 98)
        self.Button3 = Button(background = 'red', font = 'Arial 12 bold', foreground = 'white', text = 'Apagar')
        self.Button3.place(x = 505, y = 142, height = 31, width = 100)
        self.Button4 = Button(background = 'orange', font = 'Arial 12 bold', text = 'Alterar')
        self.Button4.place(x = 507, y = 102, height = 31, width = 99)
        self.Button5 = Button(font = 'Arial 12 bold', text = 'OK', )
        self.Button5.place(x = 297, y = 124, height = 47, width = 195)
        self.Entry1 = Entry(borderwidth = 3, font = 'Arial 16 bold', foreground = 'blue', justify = 'left')
        self.Entry1.place(x = 119, y = 64, height = 47, width = 380)
        self.Entry2 = Entry(borderwidth = 3, font = 'Arial 16 bold', foreground = 'blue', justify = 'left')
        self.Entry2.place(x = 117, y = 122, height = 48, width = 161)

        self.janela.mainloop()

aplicacao=App()