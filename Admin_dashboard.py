import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

def manage_doctors():
    os.system("python admin_doc_register.py")

def manage_patients():
    # Implement the logic to manage patients
    print("Managing patients...")

def manage_appointments():
    # Implement the logic to manage appointments
    print("Managing appointments...")

root = tk.Tk()
root.title("Admin Dashboard")
root.config(background='#2F6C60')

# Load the image
image = Image.open("Dashboard.png")  # Replace "Dashboard.png" with the path to your PNG image file

# Resize the image to a desired width and height
width = 500
height = 200
image = image.resize((width, height))

# Create a Tkinter-compatible photo image from the resized PIL image object
photo = ImageTk.PhotoImage(image)

# Create a label widget to display the resized image
image_label = tk.Label(root, image=photo, bg="#2F6C60")
image_label.pack()

# Create the main frame
main_frame = ttk.Frame(root, padding=60)
main_frame.pack()

# Manage Doctors button
doctors_button = ttk.Button(main_frame, text="Manage Doctors", command=manage_doctors)
doctors_button.pack(pady=10)

# Manage Patients button
patients_button = ttk.Button(main_frame, text="Discharge Patients", command=manage_patients)
patients_button.pack(pady=10)

# Manage Appointments buttons
appointments_button1 = ttk.Button(main_frame, text="View Discharge Patients", command=manage_appointments)
appointments_button1.pack(pady=10)

appointments_button2 = ttk.Button(main_frame, text="Assign Doctor to a Patient", command=manage_appointments)
appointments_button2.pack(pady=10)

appointments_button3 = ttk.Button(main_frame, text="Update Admin Details", command=manage_appointments)
appointments_button3.pack(pady=10)

appointments_button4 = ttk.Button(main_frame, text="Add Patients", command=manage_appointments)
appointments_button4.pack(pady=10)

appointments_button5 = ttk.Button(main_frame, text="Appointments", command=manage_appointments)
appointments_button5.pack(pady=10)

appointments_button6 = ttk.Button(main_frame, text="Group Patients", command=manage_appointments)
appointments_button6.pack(pady=10)

appointments_button8 = ttk.Button(main_frame, text="Request for a Report", command=manage_appointments)
appointments_button8.pack(pady=10)

appointments_button7 = ttk.Button(main_frame, text="Quit", command=manage_appointments)
appointments_button7.pack(pady=10)

root.mainloop()
