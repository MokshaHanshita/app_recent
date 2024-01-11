import tkinter as tk
from tkinter import ttk, messagebox
import requests
import tkinter as tk
import requests
import customtkinter as ctk
from PIL import Image, ImageTk
from idlelib.tooltip import Hovertip
import pandas as pd
import random
df=pd.read_csv('Info.csv')

class screen_1():
    def __init__(self, app,genre,welcome_frame):
        self.app = app
        self.welcome_frame=welcome_frame
        self.screen1_frame = ctk.CTkFrame(master=app, border_width=2, corner_radius=10, width=650, height=550)
        self.screen1_frame.place(x=30, y=30)
        result_text = tk.Label(master=self.screen1_frame, text=genre, wraplength=400)
        result_text.place(x=10,y=10)
        Quotes=[]
        b1_button = ctk.CTkButton(self.screen1_frame, text ="Back",command=self.Back_func)
        b1_button.place(x=500,y=10)
        for index,rows in df.iterrows():
            if genre in rows['category']:
                Quotes.append(rows['quote'])
        print(Quotes)
        posy=50
        if len(Quotes)<=2:
            for x in range(len(Quotes)):
                text_label = ctk.CTkLabel(self.screen1_frame, text=Quotes[x], font=("Arial", 16),wraplength=400)
                text_label.place(x=50,y=100)
        else:
            temp=random.choice(Quotes)
            temp_list=[]
            temp_list.append(temp)
            for x in range(len(temp_list)):
                text_label = ctk.CTkLabel(self.screen1_frame, text=temp_list[x], font=("Arial", 16),wraplength=400)
                text_label.place(x=30,y=posy)
                posy=posy+50
    def Back_func(self):
        self.screen1_frame.place_forget()
        self.welcome_frame.place(x=30, y=30)
