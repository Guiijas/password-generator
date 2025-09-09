import tkinter
import random
import string
from api_generator import Password_Generator



class PassWordGUI:
    def __init__(self):
    

        self.root = tkinter.Tk()

        self.root.geometry("700x500")
        self.root.title("Password Generator")

        self.label = tkinter.Label(self.root, text="Customize sua senha preenchendo os campos abaixo:", font=('Arial', 18, 'bold'))
        self.label.pack(padx=20, pady=20)

        self.label2 = tkinter.Label(self.root, text="Qual o comprimento da senha que deseja?", font=('Arial', 12))
        self.label2.pack(padx=10, pady=10)
        
        self.password_size_var = tkinter.StringVar()
        self.first_entry = tkinter.Entry(self.root, width=10, textvariable=self.password_size_var)
        self.first_entry.pack(pady=5)

        self.label3 = tkinter.Label(self.root, text="Deseja que a senha contenha caracteres?", font=('Arial', 12))
        self.label3.pack(padx=10, pady=10)

        self.check_state1 = tkinter.IntVar(value=1)
        
        tkinter.Radiobutton(self.root, text='sim', variable=self.check_state1, value=1).pack()
        tkinter.Radiobutton(self.root, text='nao', variable=self.check_state1, value=0).pack()

        self.label4 = tkinter.Label(self.root, text="Deseja que a senha contenha caracteres especiais?", font=('Arial', 12))
        self.label4.pack(padx=5, pady=10)

        self.check_state2 = tkinter.IntVar(value=1)

        tkinter.Radiobutton(self.root, text='sim', variable=self.check_state2, value=1).pack()
        tkinter.Radiobutton(self.root, text='nao', variable=self.check_state2, value=0).pack()


        self.button = tkinter.Button(self.root, text="Gerar Senha", font=('Arial', 18), command=self.gerar_senha)
        self.button.pack(padx=10, pady=30)

        self.root.mainloop()

    def gerar_senha(self):
        tamanho = int(self.password_size_var.get())
        tem_caracteres = bool(self.check_state1.get())
        tem_especial = bool(self.check_state2.get())

        senha = Password_Generator(password_size=tamanho, check_ch=tem_caracteres, check_special=tem_especial)
        print(senha)


GUi = PassWordGUI()