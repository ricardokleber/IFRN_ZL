from tkinter import *


class App:
    def __init__(self):
        self.janela = Tk()
        self.janela.title("Agenda")
        self.janela.geometry('300x150')

        self.contatos = {}

        self.frame1 = Frame(self.janela)
        self.frame1.pack()

        self.label1 = Label(self.frame1, text="Insira Contatos na Agenda:")
        self.label1.pack(pady=10)

        self.frame2 = Frame(self.janela)
        self.frame2.pack()

        self.label2 = Label(self.frame2, text="Nome:")
        self.label2.pack(side=LEFT, pady=5)

        self.caixa2 = Entry(self.frame2)
        self.caixa2.pack(side=LEFT)

        self.frame3 = Frame(self.janela)
        self.frame3.pack()

        self.label3 = Label(self.frame3, text="Telefone:")
        self.label3.pack(side=LEFT, pady=5)

        self.caixa3 = Entry(self.frame3)
        self.caixa3.pack(side=LEFT)

        self.frame4 = Frame(self.janela)
        self.frame4.pack()

        self.botao1 = Button(text="Inserir",command=self.inserir)
        self.botao1.pack(pady=5)

        self.janela.mainloop()

    def inserir(self):
        self.contatos[self.caixa2.get()] = self.caixa3.get()
        print(self.contatos)

aplicacao = App()
