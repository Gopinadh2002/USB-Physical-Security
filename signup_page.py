import os
from customtkinter import *
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter import PhotoImage
from tkinter import Label
import hashlib
import time
import re

root=CTk()
root.title("SIGN-UP")
root.geometry("800x600")
set_appearance_mode='light'

    # Load the image using Pillow
image_path = "newgrey.png"  # Make sure this path is correct and the file exists
image = Image.open(image_path)

    # Convert the image to PhotoImage for use with Tkinter
photo = ImageTk.PhotoImage(image)

    # Create a Label widget to display the image
background_label = Label(root, image=photo)

    # Position the label with the image as the full background
background_label.place(x=0, y=0, relwidth=1, relheight=1)

    # Keep a reference to the image to avoid it being garbage-collected
background_label.image = photo


# ... (rest of your code for background image remains the same)
head_label = CTkLabel(master=root, text='SIGN UP FOR USB SECURITY APPLICATION', font=("Arial", 30, "bold","underline"),  text_color='#328ad6')
head_label.place(relx=0.5, rely=0.10, anchor="n")

# Define text labels and entry fields with proper placement
first_name_label = CTkLabel(master=root, text="Enter the first name:", font=("Helvetica", 20, "bold"), text_color='#f74f20')
first_name_label.place(relx=0.19, rely=0.25, anchor="n")
first_name_entry = CTkEntry(master=root, placeholder_text="Enter here", width=300, text_color="#FFCC70", corner_radius=15)
first_name_entry.place(relx=0.5, rely=0.25, anchor="n")
first_name_entry.configure(bg_color="#242424")

# Last Name
last_name_label = CTkLabel(master=root, text="Enter the last name:", font=("Quicksand", 20, "bold"), text_color='#f74f20')
last_name_label.place(relx=0.19, rely=0.35, anchor="n")
last_name_entry = CTkEntry(master=root, placeholder_text="Enter here", width=300, text_color="#FFCC70", corner_radius=15)
last_name_entry.place(relx=0.5, rely=0.35, anchor="n")

# Email
email_label = CTkLabel(master=root, text="Enter your email:", font=("Quicksand", 20, "bold"), text_color='#f74f20')
email_label.place(relx=0.17, rely=0.45, anchor="n")
email_entry = CTkEntry(master=root, placeholder_text="Enter here", width=300, text_color="#FFCC70", corner_radius=15)
email_entry.place(relx=0.5, rely=0.45, anchor="n")

# Password
password_label = CTkLabel(master=root, text="Enter password:", font=("Quicksand", 20, "bold"), text_color='#f74f20')
password_label.place(relx=0.168, rely=0.55, anchor="n")
password_entry = CTkEntry(master=root, placeholder_text="Enter here", width=300, text_color="#FFCC70", show="*", corner_radius=15)
password_entry.place(relx=0.5, rely=0.55, anchor="n")


lbl=CTkLabel( master=root,text="Gender :" ,font=("Helvetica", 20, "bold"), text_color='#f74f20')
lbl.place(relx=0.168,rely=0.65,anchor="n")

options= CTkComboBox( master =root,values=["select","Male","Female","other"],font=("helvetica",13),state='readonly',justify=CENTER)
options.place(relx=0.44,rely=0.65,anchor="n")

label_status = CTkLabel(root, text="",text_color="red")
label_status.pack(pady=10)

# converting the data to hash code
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to save username and hashed password to a .dat file
def save_credentials(username, password, first_name, last_name, gender):
    with open('credentials.dat', 'a') as file:
        file.write(f"{hash_password(username)},{hash_password(password)}, {hash_password(first_name)}, {hash_password(last_name)},{hash_password(gender)}\n")

def validate_password(password):
    if len(password) < 8:
        return False
    if not re.search("[a-z]", password):
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    if not re.search("[_@$]", password):
        return False
    return True

# Function to handle the registration process
def validate_email(email):
    email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.match(email_regex, email):
        return True
    else:
        return False

def register():
    username = email_entry.get()
    password = password_entry.get()
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    gender = options.get()

    if username and password and first_name and last_name and gender: 
        if validate_email(username):
            if validate_password(password):
                save_credentials(username, password, first_name, last_name, gender)
                label_status.configure(text="Registration Successful")
                root.after(2000, root.destroy)
            else:
                label_status.configure(text="Password must be at least 8 characters long and contain uppercase, lowercase, numbers, and special characters")
        else:
            label_status.configure(text="Invalid email address")
    else:
        label_status.configure(text="Please enter all the fields")
        reset_fields()

    reset_fields()
            

btn =CTkButton(master=root, text="Log in",corner_radius=32, fg_color="green",
               hover_color="dark green", border_color="#242424", border_width=2,command=register)
btn.place(relx=0.5, rely=0.75, anchor="center")

def reset_fields():
    first_name_entry.delete(0, END)
    last_name_entry.delete(0, END)
    email_entry.delete(0, END)
    password_entry.delete(0, END)
    options.set("")

root.mainloop()
