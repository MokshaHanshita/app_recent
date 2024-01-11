

from threading import Thread
import time
import customtkinter as ctk 
from login_register import LoginAndRegister
from home import Home


        
# Selecting GUI theme - dark,  
# light , system (for system default) 
ctk.set_appearance_mode("dark") 
  
# Selecting color theme-blue, green, dark-blue 
ctk.set_default_color_theme("blue") 


app = ctk.CTk() 
app.geometry("700x600") 
app.resizable(False,False)
app.title("Quotes Generator") 
def show_home_page(name):
    home_obj=Home(app,name)
login_obj=LoginAndRegister(app)
#show_home_page("moksha")

def check_login_status():
    while True:
        status,name=login_obj.login_success()
        if status==True:
            show_home_page(name)
            break
            
        time.sleep(1)
        
    

check_thread=Thread(target=check_login_status)
check_thread.start()


app.mainloop()

        
