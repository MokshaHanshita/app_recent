import tkinter as tk
from tkinter import ttk, messagebox
import requests
import customtkinter as ctk
from PIL import ImageTk, Image
login_status=False
ausername=""

class LoginAndRegister():
    def __init__(self, app):

        self.app = app

        # Create a login_frame
        self.welcome_frame = ctk.CTkFrame(
            master=app, border_width=2, corner_radius=10, width=400, height=500)
        self.welcome_frame.place(x=20, y=70)

        # Create a login_frame
        self.login_frame = ctk.CTkFrame(
            master=app, border_width=2, corner_radius=10, width=250, height=500)
        self.login_frame.place(x=430, y=70)

        # Set the label inside the login_frame
        self.label = ctk.CTkLabel(master=self.login_frame,
                                  text='LOGIN')
        self.label.place(x=100, y=50)


        # Create the text box for taking
        # username input from user
        self.user_entry = ctk.CTkEntry(master=self.login_frame,
                                       placeholder_text="Username")
        self.user_entry.place(x=50, y=100)

        # Create a text box for taking
        # password input from user
        self.user_pass = ctk.CTkEntry(master=self.login_frame,
                                      placeholder_text="Password",
                                      show="*")
        self.user_pass.place(x=50, y=150)

        # Create a login button to login
        self.button = ctk.CTkButton(master=self.login_frame,
                                    text='Login', command=self.perform_login)
        self.button.place(x=50, y=200)

        # Create a register button to register
        self.register = ctk.CTkButton(master=self.login_frame,
                                      text='New User?', command=self.show_register_frame)
        self.register.place(x=50, y=250)

    def perform_login(self):
        global ausername
        global login_status
        check_counter = 0
        if self.user_entry.get() == "":
            warn = "Username can't be empty"
        else:
            check_counter += 1
        if self.user_pass.get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1
        if check_counter == 2:
            try:
                response = requests.post('https://mokshahanshita.pythonanywhere.com/login', {
                                         'username': self.user_entry.get(), "password": self.user_pass.get()})
                print(response)
                if(response.text=="Login successful"):
                    ausername=self.user_entry.get()
                    self.user_pass.delete(0)
                    self.user_entry.delete(0)
                    self.welcome_frame.destroy()
                    self.login_frame.destroy()
                    login_status=True
                    self.login_success()
                messagebox.showinfo("", response.text)
    

            except Exception as e:
                messagebox.showerror(e)
        else:
            messagebox.showerror('', warn)

    def show_register_frame(self):

        self.login_frame.place_forget()

        # Create a login_frame
        self.register_frame = ctk.CTkFrame(
            master=self.app, border_width=2, corner_radius=10, width=250, height=500)
        self.register_frame.place(x=430, y=70)

        # # Create a login button to login
        self.back = ctk.CTkButton(master=self.register_frame,
                                  text='Back', command=self.go_back)
        self.back.place(x=50, y=20)

        # # Set the label inside the register_frame
        self.label = ctk.CTkLabel(master=self.register_frame,
                                  text='REGISTER')
        self.label.place(x=100, y=50)

        # Create the text box for taking
        # username first and last name from user
        self.first_name_entry = ctk.CTkEntry(master=self.register_frame,
                                             placeholder_text="Enter First Name")
        self.first_name_entry.place(x=50, y=100)

        self.last_name_entry = ctk.CTkEntry(master=self.register_frame,
                                            placeholder_text="Enter Last Name")
        self.last_name_entry.place(x=50, y=150)

        self.mobile_entry = ctk.CTkEntry(master=self.register_frame,
                                         placeholder_text="Enter Mobile Number")
        self.mobile_entry.place(x=50, y=200)

        self.mail_entry = ctk.CTkEntry(master=self.register_frame,
                                       placeholder_text="Enter email address")
        self.mail_entry.place(x=50, y=250)

        # # Create a text box for taking
        # # password input from user
        self.pass_entry = ctk.CTkEntry(master=self.register_frame,
                                       placeholder_text="Enter Password",
                                       show="*")
        self.pass_entry.place(x=50, y=300)

        self.pass_again_entry = ctk.CTkEntry(master=self.register_frame,
                                             placeholder_text=" Confirm Password",
                                             show="*")
        self.pass_again_entry.place(x=50, y=350)

        # Create a login button to login
        self.button = ctk.CTkButton(master=self.register_frame,
                                    text='Register', command=self.register_user)
        self.button.place(x=50, y=400)

    def register_user(self):
        check_counter = 0
        warn = ""
        if self.first_name_entry.get() == "":
            warn = "Name can't be empty"
        else:
            check_counter += 1

        if self.mail_entry.get() == "":
            warn = "Email can't be empty"
        else:
            check_counter += 1

        if self.mobile_entry.get() == "":
            warn = "Contact can't be empty"
        else:
            check_counter += 1

        if self.pass_entry.get() == "":
            warn = "Password can't be empty"
        else:
            check_counter += 1

        if self.pass_again_entry.get() == "":
            warn = "Re-enter password can't be empty"
        else:
            check_counter += 1

        if self.pass_entry.get() != self.pass_again_entry.get():
            warn = "Passwords didn't match!"
        else:
            check_counter += 1
        print(check_counter)
        if check_counter == 6:
            try:
                response = requests.post('https://mokshahanshita.pythonanywhere.com/register', {
                                         'username': self.mail_entry.get(), "password": self.pass_entry.get()})
                print(response)
                messagebox.showinfo('confirmation', 'Record Saved')
                ausername=self.mail_entry.get()
                self.first_name_entry.delete(0)
                self.last_name_entry.delete(0)
                self.mail_entry.delete(0)
                self.mobile_entry.delete(0)
                self.pass_entry.delete(0)
                self.pass_again_entry.delete(0)
                self.go_back()

            except Exception as ep:
                messagebox.showerror('', ep)
                print(ep)
        else:
            messagebox.showerror('Error', warn)

    def go_back(self):

        self.login_frame.place(x=430, y=70)
        self.register_frame.place_forget()
        
    def login_success(self):
        global login_status,ausername
        return login_status,ausername
