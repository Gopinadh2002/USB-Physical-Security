import tkinter as tk
from tkinter import messagebox
import subprocess
import webbrowser
import base64
from PIL import Image, ImageTk
from tkinter import Tk,PhotoImage
import io
import tempfile
import sys
import os

password = "password"

icon_path= 'logo.png'

base64_icon = ' '

icon_data = base64.b64decode(base64_icon)

root=tk.Tk()
root.geometry("500x500")
icon_image = PhotoImage(data=icon_data)
root.iconphoto(True,icon_image)
root.title("USB Phusical Security For Systems")
button1 = root.Button(text= "Enable",command=button1_clicked)
button1.geometry("200x100").pack()
button2 = root.Button(text= "Disable",command=button2_clicked)


def button2_clicked():
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password.label = tk.Label(password_windows,text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    def ok_button():
        if password_entry.get()==password:
            subprocess.run([r'unblock_usb.bat'], text=True)
            password_window.destory()
            sucess_label.config(text="USB Ports Enabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please Try again.")
            password_entry.delete(0,tk.END)
    ok_button = tk.Button(password_window, text="Ok", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, texxt="", font=("Arial",12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

def button1_clicked():
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password.label = tk.Label(password_windows,text="Enter Password:")
    password_label.pack()
    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack()
    def ok_button():
        if password_entry.get()==password:
            subprocess.run([r'block_usb.bat'],text=true)
            password_window.destroy()
            success_label.config(test="USB Ports Disabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0,tk.END)
    ok_button = tk.Button(password_window, text="OK", command=ok_button)
    ok_button.pack()
    error_label = tk.Label(password_window, text="", font=("Arial",12), bg="#f2f2f2", fg="#ff0000")
    error_label.pack()

root.mainloop()
