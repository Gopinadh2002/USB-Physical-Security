import tkinter as tk
import subprocess
from PIL import Image, ImageTk

# Define your password here
PASSWORD = "your_password"

# Initialize the main window
root = tk.Tk()
root.title("USB Control")
root.geometry("600x500")
root.configure(bg="black")

# Load the image
image_path = "/mnt/data/WhatsApp Image 2024-06-22 at 13.50.10_755b1101.jpg"
image = Image.open(image_path)
image = image.resize((100, 100), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)

# Display the image
image_label = tk.Label(root, image=photo, bg="black")
image_label.pack(pady=20)

# Success label for displaying results
success_label = tk.Label(root, text="", font=("Arial", 12), bg="black", fg="#00ff00")
success_label.pack(pady=20)

def create_password_window(command):
    password_window = tk.Toplevel(root)
    password_window.title("Enter Password")
    password_window.geometry("300x200")
    password_window.configure(bg="black")

    password_label = tk.Label(password_window, text="Enter Password:", bg="black", fg="white")
    password_label.pack(pady=10)

    password_entry = tk.Entry(password_window, show="*")
    password_entry.pack(pady=10)

    error_label = tk.Label(password_window, text="", font=("Arial", 12), bg="black", fg="#ff0000")
    error_label.pack(pady=10)

    def ok_button_clicked():
        if password_entry.get() == PASSWORD:
            subprocess.run([command], text=True)
            password_window.destroy()
            if command == r'block_usb.bat':
                success_label.config(text="USB Ports Disabled Successfully")
            else:
                success_label.config(text="USB Ports Enabled Successfully")
        else:
            error_label.config(text="Incorrect password. Please try again.")
            password_entry.delete(0, tk.END)

    ok_button = tk.Button(password_window, text="OK", command=ok_button_clicked, bg="white", fg="black")
    ok_button.pack(pady=10)

def button1_clicked():
    create_password_window(r'block_usb.bat')

def button2_clicked():
    create_password_window(r'unblock_usb.bat')

# Buttons for disabling and enabling USB
button_frame = tk.Frame(root, bg="black")
button_frame.pack(pady=20)

button1 = tk.Button(button_frame, text="Disable USB", command=button1_clicked, bg="white", fg="black")
button1.pack(side="left", padx=20)

button2 = tk.Button(button_frame, text="Enable USB", command=button2_clicked, bg="white", fg="black")
button2.pack(side="right", padx=20)

root.mainloop()
