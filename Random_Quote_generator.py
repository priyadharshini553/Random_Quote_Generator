import tkinter as tk
import random

quotes = [
    "Believe in yourself.",
    "Success comes through hard work.",
    "Never stop learning.",
    "Dream big and work hard.",
    "Stay positive and keep smiling."
]

def show_quote():
    quote = random.choice(quotes)
    label.config(text=quote)

root = tk.Tk()
root.title("Random Quote Generator")
root.geometry("500x300")

label = tk.Label(root, text="Click the button to get a quote", wraplength=400, font=("Arial", 14))
label.pack(pady=40)

button = tk.Button(root, text="Generate Quote", command=show_quote)
button.pack()

root.mainloop()