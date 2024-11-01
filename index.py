from tkinter import *
from customtkinter import*
import subprocess
import webbrowser
from PIL import Image, ImageTk
import os
import hashlib


root = Tk()
root.title("USB Project")
root.configure(background="black")
root.geometry("470x500")

def open_website():
    webbrowser.open("projectinfo.html")

image = Image.open("pen7.png")
resized_image = image.resize((150,250))
photo = ImageTk.PhotoImage(resized_image)
label = Label(root, image=photo, borderwidth=0, highlightthickness=0, cursor="hand2")
label.bind("<Button-1>", lambda event: open_website())
label.place(relx=0.5, rely=0.3, anchor='center') 

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

file_path = 'credentials.dat'
    
def display_log():
    log_window = Toplevel(root)
    log_window.title("Log File")
    log_window.geometry("600x300")

    log_text_widget = Text(log_window, width=40, height=15)
    log_text_widget.pack(side="left", fill="both", expand=True)

    log_scrollbar = Scrollbar(log_window, orient="vertical", command=log_text_widget.yview)
    log_scrollbar.pack(side="right", fill="y")

    log_text_widget.config(yscrollcommand=log_scrollbar.set)

    if os.path.exists("login_log.txt"):
        with open("login_log.txt", "r", encoding="utf-8") as f:
            log_text = f.read()
        log_text_widget.insert("1.0", log_text)

log_button = CTkButton(master=root, text="View Log", corner_radius=30, fg_color="Yellow", text_color="Red", width=200, height=50,
                       hover_color="black", border_color="black", border_width=2, font=("Segoe UI", 15, "bold"),
                       command=display_log)
log_button.place(relx=0.5, rely=0.85, anchor="center")

def button1_clicked():
    password_window = Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password_label = Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = Entry(password_window, show="*")
    password_entry.pack()

    def ok_button():
        if not os.path.exists(file_path):
            error_label.config(text="Credentials file not found.")
            return
        
        with open(file_path, 'r') as file:
            for line in file:
                stored_email, stored_password, first_name, last_name, gender = line.strip().split(',')
                entered_password = hash_password(password_entry.get())
                if entered_password == stored_password:
                    subprocess.run([r"unblock_usb.bat"], shell=True)
                    password_window.destroy()
                    success_label = Label(root, text="USB Ports Enabled Successfully")
                    success_label.pack()
                    return
            error_label.config(text="Incorrect Password. Please Try Again.")
            password_entry.delete(0, END)
    
    Ok_button = Button(password_window, text='OK', command=ok_button, background="Green")
    Ok_button.pack()
    error_label = Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

enable_button = CTkButton(root, text="ENABLE PORT", fg_color="Blue", text_color="Yellow", command=button1_clicked,
                          corner_radius=30, width=200, height=50, hover_color="dark blue", font=("Segoe UI", 15, "bold"))
enable_button.place(relx=0.5, rely=0.55, anchor="center")


def button2_clicked():
    password_window = Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password_label = Label(password_window, text="Enter Password:")
    password_label.pack()
    password_entry = Entry(password_window, show="*")
    password_entry.pack()

    def ok_button():
        if not os.path.exists(file_path):
            error_label.config(text="Credentials file not found.")
            return
        
        with open(file_path, 'r') as file:
            for line in file:
                stored_email, stored_password, first_name, last_name, gender = line.strip().split(',')
                entered_password = hash_password(password_entry.get())
                if entered_password == stored_password:
                    subprocess.run([r"block_usb.bat"], shell=True)
                    password_window.destroy()
                    success_label = Label(root, text="USB Ports Disabled Successfully")
                    success_label.pack()
                    return
            error_label.config(text="Incorrect Password. Please Try Again.")
            password_entry.delete(0, END)
    
    Ok_button = Button(password_window, text='OK', command=ok_button, background="Green")
    Ok_button.pack()
    error_label = Label(password_window, text="", font=("Arial", 12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

disable_button = CTkButton(root, text="DISABLE PORT", fg_color="Red", text_color="White", command=button2_clicked,
                           corner_radius=30, width=200, height=50, hover_color="Dark red", font=("Segoe UI", 15, "bold")) 
disable_button.place(relx=0.5, rely=0.7, anchor="center")


root.mainloop()
