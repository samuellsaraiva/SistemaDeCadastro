"""IMPORTANDO BIBLIOTECAS"""
from tkinter import *
from tkinter import messagebox, ttk
import BancoDeDados

# configurações da janela
jan = Tk()
jan.title("SSC System - Access Panel")
jan.geometry("600x300")
jan.configure(background="WHITE")
jan.resizable(width=False, height=False)  # para não possibilitar o usuário a mexer na dimensão da janela
jan.attributes("-alpha", 0.9)  # deixar a janela com fundo transparente
jan.iconbitmap(default="icons/LogoIcon.ico")  # ícone do canto superior esquerdo

'''IMAGENS'''
logo = PhotoImage(file="icons/logo.png")

'''WIDGETS'''
left_frame = Frame(jan, width=200, height=300, bg="BLACK", relief="raise")
left_frame.pack(side=LEFT)

right_frame = Frame(jan, width=395, height=300, bg="BLACK", relief="raise")
right_frame.pack(side=RIGHT)

logo_label = Label(left_frame, image=logo, bg="BLACK")
logo_label.place(x=50, y=100)

user_label = Label(right_frame, text="Nome de Usuário:", font=("Arial", 15), bg="BLACK", fg="WHITE")
user_label.place(x=5, y=10)

user_entry = ttk.Entry(right_frame, width=30)
user_entry.place(x=175, y=15)

pass_label = Label(right_frame, text="Senha:", font=("Arial", 15), bg="BLACK", fg="white")
pass_label.place(x=5, y=40)

pass_entry = ttk.Entry(right_frame, width=30, show="*")
pass_entry.place(x=175, y=45)

'''BOTÕES'''


def login():
    login_usuario = user_entry.get()
    senha_usuario = pass_entry.get()
    BancoDeDados.cur.execute("""
    SELECT * FROM TB_Usuarios
    WHERE Usuario = ? AND Senha = ?
    """, (login_usuario, senha_usuario))
    verificar_login = BancoDeDados.cur.fetchone()
    try:
        if login_usuario in verificar_login and senha_usuario in verificar_login:
            messagebox.showinfo(title="Aviso de Login", message="Acesso Confirmado!")
    except:
        messagebox.showerror(title="Erro de Login", message="Algo deu errado. Verifique os campos acima.")


login_button = ttk.Button(right_frame, text="Entrar", width=30, command=login)
login_button.place(x=100, y=225)


def register():
    # para sumir com os botões ao clicar em "Registrar"
    login_button.place(x=10000, y=10000)
    RegisterButton.place(x=10000, y=10000)

    # inserindo WIDGETS no Cadastro ao clicar em "Registrar"
    user_label.place(x=5, y=10)
    user_entry.place(x=175, y=15)

    nome_label = Label(right_frame, text="Nome:", font=("Arial", 15), bg="BLACK", fg="White")
    nome_label.place(x=5, y=40)

    nome_entry = ttk.Entry(right_frame, width=30)
    nome_entry.place(x=175, y=45)

    email_label = Label(right_frame, text="E-mail:", font=("Arial", 15), bg="BLACK", fg="White")
    email_label.place(x=5, y=70)

    email_entry = ttk.Entry(right_frame, width=30)
    email_entry.place(x=175, y=75)

    pass_label.place(x=5, y=100)
    pass_entry.place(x=175, y=105)

    # para retirar os dados de entrada
    pass_entry.delete(0, END)
    user_entry.delete(0, END)
    nome_entry.delete(0, END)
    email_entry.delete(0, END)

    def register_to_database():
        # pegando os dados inseridos pelo usuário e inserindo na base de dados
        nome = nome_entry.get()
        email = email_entry.get()
        usuario = user_entry.get()
        senha = pass_entry.get()

        if nome == "" or email == "" or usuario == "" or senha == "":
            messagebox.showerror(title="Erro de Registro", message="Preencha todos os campos corretamente")
        else:
            BancoDeDados.cur.execute("""
                INSERT INTO TB_Usuarios (Nome, Email, Usuario, Senha) VALUES (?, ?, ?, ?)
            """, (nome, email, usuario, senha))
            BancoDeDados.conn.commit()
            messagebox.showinfo(title="Informações de Registro", message="Conta criada com sucesso!")
            back_to_login()

    register_button = ttk.Button(right_frame, text="Registrar", width=30, command=register_to_database)
    register_button.place(x=100, y=225)

    def back_to_login():
        # para sumir com o Widget de Cadastro
        nome_label.place(x=10000)
        nome_entry.place(x=10000)
        email_label.place(x=10000)
        email_entry.place(x=10000)
        register_button.place(x=10000)
        back.place(x=10000)
        # trazendo de volta os Widgets de Login
        login_button.place(x=100, y=225)
        RegisterButton.place(x=100, y=260)
        pass_label.place(x=5, y=40)
        pass_entry.place(x=175, y=45)
        pass_entry.delete(0, END)
        user_entry.delete(0, END)

    back = ttk.Button(right_frame, text="Voltar", width=30, command=back_to_login)
    back.place(x=100, y=260)


RegisterButton = ttk.Button(right_frame, text="Registrar", width=30, command=register)
RegisterButton.place(x=100, y=260)

jan.mainloop()
