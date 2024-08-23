from tkinter import Tk, Label, Button
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Splash Screen!!")
root.geometry("1000x700")
root.minsize(1400, 700)
root.overrideredirect(False)
root.config(background='#2F6C60')

welcome_label = Label(text="Welcome Back!", bg="#2F6C60", font=("Trebuchet Ms", 27, "bold"), fg="#FFFFFF")
welcome_label.place(x=220, y=70)

welcome_label2 = Label(text="Click The button", bg="#2F6C60", font=("Trebuchet Ms", 20, "bold"), fg="#FFFFFF")
welcome_label2.place(x=230, y=125)


def top_Admin():
    root.withdraw()
    os.system("python Admin_dashboard.py")
    root.destroy()

# Load images
patient_image = Image.open("gif\patient.gif").resize((300, 200), Image.ANTIALIAS)
doctor_image = Image.open("gif\doctor.gif").resize((300, 200), Image.ANTIALIAS)
admin_image = Image.open("gif\\admin.gif").resize((300, 200), Image.ANTIALIAS)

admin_image = ImageTk.PhotoImage(admin_image)

admin_button = Button(root, text="Admin", image=admin_image, compound="top", command=top_Admin)
admin_button.place(x=500, y=225)

root.mainloop()
