import tkinter as tk
from tkinter import messagebox
import time

def check_weather():
    location = entry.get().strip()
    if not location:
        messagebox.showwarning("Warning", "Please enter a location!")
        return
    
    status_label.config(text="Searching location...")
    root.update()
    time.sleep(2)
    
    status_label.config(text="Analyzing the clouds...")
    root.update()
    time.sleep(2)
    
    messagebox.showinfo("AI Weather Forecast", "Idk, just look outside.")

root = tk.Tk()
root.title("Crazy AI Weather Forecast")
root.geometry("300x200")

label = tk.Label(root, text="Enter your location:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=5)

button = tk.Button(root, text="Check weather", command=check_weather)
button.pack(pady=10)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
