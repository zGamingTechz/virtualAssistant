import tkinter as tk
from tkinter import font

# Definitions
root = tk.Tk()
root.title("Lisa (Llama 2 7b)")
root.geometry("400x540")

# Layout
heading = tk.Label(root, text="Lisa 👩🏻‍💻", font=(font.BOLD, 20))
heading.pack_configure(pady=20)

textbox = tk.Text(root, height=3, font=("Helvetica", 20, "bold"), borderwidth=2, relief=tk.SOLID)
textbox.pack_configure(side=tk.BOTTOM, padx=3, pady=3)


root.mainloop()
