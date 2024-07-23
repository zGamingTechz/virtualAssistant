import tkinter as tk
from tkinter import font

#---Definitions---
root = tk.Tk()
root.title("Lisa (Llama 2 7b)")
root.geometry("400x540")

#---Layout---
heading = tk.Label(root, text="Lisa 👩🏻‍💻", font=(font.BOLD, 20))
heading.pack_configure(pady=20)

#frame for button and textbox
frame = tk.Frame(root)
frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

send_button = tk.Button(frame, text="Send 📩", font=(font.BOLD, 15))
send_button.pack_configure(side=tk.RIGHT, padx=7)

textbox = tk.Text(frame, height=2, font=("Helvetica", 20, "bold"), borderwidth=2, relief=tk.SOLID)
textbox.pack_configure(side=tk.LEFT, padx=3, pady=3)


root.mainloop()
