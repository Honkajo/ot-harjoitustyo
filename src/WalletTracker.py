from tkinter import *
import os
import tkinter as tk
from gui import WalletTrackerGUI

current_user = None

def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Kirjautuminen")
    Button(text="Kirjaudu", height="2", width="30", command=login).pack(pady=(60, 0))
    Button(text="Rekisteröidy", height="2",
           width="30", command=register).pack(pady=(20, 0))

    main_screen.mainloop()

def login():
    global login_screen
    global username_verify
    global password_verify
    global username_login_entry
    global password_login_entry
    
    login_screen = Toplevel(main_screen)
    login_screen.title("Kirjaudu sisään")
    login_screen.geometry("300x250")
    Label(login_screen, text="Syötä käyttäjätunnus ja salasana").pack()
    Label(login_screen, text="").pack()
    username_verify = StringVar()
    password_verify = StringVar()
    Label(login_screen, text="Käyttäjätunnus").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Salasana").pack()
    password_login_entry = Entry(
        login_screen, textvariable=password_verify, show="*")
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Kirjaudu", width=10,
           height=1, command=login_verify).pack()


def register():
    global register_screen
    global username
    global password
    global username_entry
    global password_entry
    
    register_screen = Toplevel(main_screen)
    register_screen.title("Rekisteröidy")
    register_screen.geometry("300x250")

    username = StringVar()
    password = StringVar()

    Label(register_screen, text="Syötä käyttäjätunnus ja salasana").pack()
    username_label = Label(register_screen, text="Käyttäjätunnus")
    username_label.pack(pady=(10, 0))
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_label = Label(register_screen, text="Salasana")
    password_label.pack(pady=(10, 0))
    password_entry = Entry(register_screen, textvariable=password, show="*")
    password_entry.pack()
    Button(register_screen, text="Rekisteröidy", width=10,
           height=1, command=register_user).pack()
    
def login_verify():
    global username_verify
    global password_verify
    global current_user

    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)

    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            current_user = username1
            login_success()

        else:
            password_not_recognised()
    else:
        user_not_found()

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()

    with open(f"{username_info}_transactions.txt", "w") as trans_file:
        pass

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

    tk.Label(register_screen, text="Rekisteröinti onnistui",
             fg="green", font=("calibri", 11)).pack()

def login_success():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Kirjautuminen onnistui!")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Kirjautuminen onnistui!").pack()
    Button(login_success_screen, text="OK", command=lambda: move_to_account(current_user)).pack()


def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Onnistui!")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Väärä salasana!").pack()
    Button(password_not_recog_screen, text="OK",
           command=delete_password_not_recognised_screen).pack()


def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Onnistui!")
    user_not_found_screen.geometry("200x100")
    Label(user_not_found_screen, text="Käyttäjätunnusta ei löydy").pack()
    Button(user_not_found_screen, text="OK",
           command=delete_user_not_found_screen).pack()

def delete_login_success():
    login_success_screen.destroy()


def delete_password_not_recognised_screen():
    password_not_recog_screen.destroy()


def delete_user_not_found_screen():
    user_not_found_screen.destroy()

def move_to_account(current_user):
    login_success_screen.destroy()
    main_screen.destroy()
    transactions_file = f"{current_user}_transactions.txt"
    budget_gui = WalletTrackerGUI(transactions_file)
    budget_gui.mainloop()

main_account_screen()
