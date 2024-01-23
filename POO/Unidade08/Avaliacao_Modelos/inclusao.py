from tkinter import *

class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title('Inclusão de Alunos')
        self.janela.geometry("540x230")
        self.janela.resizable(width = False, height = False)

        self.Label1 = Label(self.janela, font = 'Arial 16 bold', text = 'Matrícula:')
        self.Label1.place(x = 13, y = 22, height = 30, width = 130)
        self.Entry1 = Entry(self.janela, font = 'Arial 16 bold', foreground = 'Red')
        self.Entry1.place(x = 137, y = 21, height = 32, width = 198)
        self.Label2 = Label(self.janela,font = 'Arial 16 bold', text = 'Nome do Aluno:')
        self.Label2.place(x = 13, y = 68, height = 30, width = 194)
        self.Entry2 = Entry(self.janela, font = 'Arial 16 bold', foreground = 'Blue')
        self.Entry2.place(x = 199, y = 69, height = 30, width = 311)
        self.Button1 = Button(self.janela,font = 'Arial 12 bold', text = 'Incluir Aluno no Banco de Dados')
        self.Button1.place(x = 22, y = 116, height = 36, width = 488)
        self.Label3 = Label(self.janela,background = 'Gray', text = '')
        self.Label3.place(x = 22, y = 168, height = 35, width = 488)

        self.janela.mainloop()

aplicacao = App()