import tkinter as tk
from tkinter import ttk, messagebox
import requests
import customtkinter as ctk
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
login_status=False
from screen1 import screen_1
genre=""
class Home():
    def __init__(self, app,name):

        self.app = app

      
        self.welcome_frame = ctk.CTkFrame(
            master=app, border_width=2, corner_radius=10, width=650, height=550)
        self.welcome_frame.place(x=30, y=30)

        # making the elements
        self.label = ctk.CTkLabel(master=self.welcome_frame,
                                  text="Hi "+name + " !!",anchor="w")
        # griding the elements
        self.label.place(x=500, y=50)
        self.label1 = ctk.CTkLabel(master=self.welcome_frame,
                                  text='Quote generator',font=("Arial", 30))
        self.label1.place(x=150, y=10)
        image1 = Image.open("icons\love.png").resize((100,100))
        tk_image1 = ImageTk.PhotoImage(image1)
        image_button1 = ctk.CTkButton(master=self.welcome_frame, text="Love", image=tk_image1,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"love"),text_color="#000000")
        
        image2 = Image.open("icons\cool.png").resize((100,100))
        tk_image2 = ImageTk.PhotoImage(image2)
        image_button2 = ctk.CTkButton(master=self.welcome_frame, text="Cool", image=tk_image2,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"cool"),text_color="#000000")

        
        image3 = Image.open("icons\History.png").resize((100,100))
        tk_image3 = ImageTk.PhotoImage(image3)
        image_button3 = ctk.CTkButton(master=self.welcome_frame, text="History", image=tk_image3,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"History"),text_color="#000000")
        
        image4 = Image.open("icons\inspirational.png").resize((100,100))
        tk_image4 = ImageTk.PhotoImage(image4)
        image_button4 = ctk.CTkButton(master=self.welcome_frame, text="Inspirational", image=tk_image4,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"Inspirational"),text_color="#000000")
        
        image5 = Image.open("icons\gratitude.png").resize((100,100))
        tk_image5 = ImageTk.PhotoImage(image5)
        image_button5 = ctk.CTkButton(master=self.welcome_frame, text="Gratitude", image=tk_image5,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"Gratitude"),text_color="#000000")
        
        image6 = Image.open("icons\patience.png").resize((100,100))
        tk_image6 = ImageTk.PhotoImage(image6)
        image_button6 = ctk.CTkButton(master=self.welcome_frame, text="Patience", image=tk_image6,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"patience"),text_color="#000000")

        image7 = Image.open("icons\life.png").resize((100,100))
        tk_image7 = ImageTk.PhotoImage(image7)
        image_button7 = ctk.CTkButton(master=self.welcome_frame, text="Life", image=tk_image7,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"life"),text_color="#000000")
        image_button8 = ctk.CTkButton(master=self.welcome_frame, text="search", image=tk_image7,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,),text_color="#000000")

        image8 = Image.open("icons\mindfulness.png").resize((100,100))
        tk_image8 = ImageTk.PhotoImage(image8)
        image_button8 = ctk.CTkButton(master=self.welcome_frame,text="Mindfulness",image=tk_image8,fg_color="#b7e8ed",hover_color="#C77C78",height=100,width=100,command=lambda:self.show_screen1(app,"mindfulness"),text_color="#000000")
        self.label2 = ctk.CTkLabel(master=self.welcome_frame,
                                  text='Did not find the wished quote search below :',font=("Arial", 20))
        self.label3 = ctk.CTkLabel(master=self.welcome_frame,
                                  text='Search By Genre',font=("Arial", 20))
        self.user_entry1 = ctk.CTkEntry(master=self.welcome_frame,
                                       placeholder_text="Enter the genre")
        self.label4 = ctk.CTkLabel(master=self.welcome_frame,
                                  text='OR',font=("Arial", 20))
        self.label5 = ctk.CTkLabel(master=self.welcome_frame,
                                  text='Search By Author',font=("Arial", 20))
        self.user_entry2 = ctk.CTkEntry(master=self.welcome_frame,
                                       placeholder_text="Enter the Author Name",width=180)
        #search_button2 = ctk.CTkButton(master=self.welcome_frame, text="search by author",height=50,width=100,command=lambda:self.show_screen1(app,author),text_color="#000000")
        search_button1 = ctk.CTkButton(master=self.welcome_frame, text="search by genre",height=50,width=100,command=lambda:self.show_screen1(app,self.user_entry1.get()),text_color="#000000")

        #search_button2.place(x=400,y=500)
        search_button1.place(x=400,y=400)
        
        
        self.user_entry1.place(x=180, y=400)
        self.label2.place(x=100, y=360)
        image_button1.place(x=20,y=100)
        image_button2.place(x=150,y=100)
        image_button3.place(x=280,y=100)
        image_button4.place(x=420,y=100)
        image_button5.place(x=20,y=250)
        image_button6.place(x=180,y=250)
        image_button7.place(x=330,y=250)
        image_button8.place(x=450,y=250)
        self.label3.place(x=10,y=400)
        self.label4.place(x=310,y=450)
        self.label5.place(x=10,y=500)
        self.user_entry2.place(x=180,y=500)
    def show_screen1(self,app,genre):
        self.welcome_frame.place_forget()
        screen1_obj=screen_1(app,genre,self.welcome_frame)

        