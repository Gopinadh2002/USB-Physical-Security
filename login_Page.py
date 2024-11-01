from customtkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import subprocess
import hashlib
import os
import logging


root= CTk()
root.title("USB Physical Security")
root.geometry("500x400")
set_appearance_mode("light")



# Labels
email_label = CTkLabel(master=root, text="Enter Email:", font=("Arial", 12), text_color="black")
email_label.place(relx=0.3, rely=0.09, anchor="w")

password_label = CTkLabel(master=root, text="Password:", font=("Arial", 12), text_color="black")
password_label.place(relx=0.3, rely=0.29, anchor="w")

# Entry Fields
email_entry = CTkEntry(master=root, placeholder_text="EMAIL", width=200, corner_radius=15)
email_entry.place(relx=0.5, rely=0.15, anchor="center")

password_entry = CTkEntry(master=root, placeholder_text="PASSWORD", show="*", width=200, corner_radius=15)
password_entry.place(relx=0.5, rely=0.35, anchor="center")



# here we store the login details 
log_file = "login_log.txt"
if not os.path.exists(log_file):
    open(log_file, "w").close()

# Configure logging
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Function to hash passwords
def hash_password(password):
   return hashlib.sha256(password.encode()).hexdigest()

# Function to check credentials for login
def check_credentials(username, password):
    file_path = 'credentials.dat'
    if not os.path.exists(file_path):
        return False
    with open(file_path, 'r') as file:
        for line in file:
            stored_email, stored_password, first_name, last_name, gender = line.strip().split(',')
            if stored_email == hash_password(username) and stored_password == hash_password(password):
                return True
    return False

#performing the login function
def login():
    username = email_entry.get()
    password = password_entry.get()

    if check_credentials(username, password): 
        label_status.configure(text="Login Successful")
        logging.info(f"Login Successful for user: {username}")
        logging.info(f"Login details: Username={username}")
        subprocess.run("python index.py")
    else: 
        label_status.configure(text="Invalid Credentials")
        logging.warning(f"Invalid Credentials for user: {username}")
        logging.warning(f"Invalid login attempt: Username={username}")
        reset_fields()

label_status = CTkLabel(root, text="")
label_status.pack(pady=10)

btn =CTkButton(master=root, text="Log in",  width=120,cursor="hand2",corner_radius=10)
btn.place(relx=0.5, rely=0.55, anchor="center")
btn.configure(command=login)


def on_label_click():
   subprocess.run("python signup_page.py")


my_label=CTkLabel(master=root, text="Register", fg_color="orange", width=120,cursor="hand2",corner_radius=10)
my_label.bind("<Button-1>", lambda event: on_label_click())
my_label.place(relx=0.5, rely=0.65, anchor="center")

def reset_fields():
    email_entry.delete(0,END)
    password_entry.delete(0, END)

root.mainloop()
