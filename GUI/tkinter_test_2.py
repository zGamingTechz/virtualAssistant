import tkinter as tk
from tkinter import font


class App:
    def __init__(self):
        #---Definitions---
        self.root = tk.Tk()
        self.root.title("Lisa (Llama 2 7b)")
        self.root.geometry("400x540")

        #---Layout---
        self.heading = tk.Label(self.root, text="Lisa 👩🏻‍💻", font=(font.BOLD, 20))
        self.heading.pack_configure(pady=20)

        #frame for button and textbox
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.BOTTOM, fill=tk.X, padx=10, pady=10)

        self.send_button = tk.Button(self.frame, text="Send 📩", font=(font.BOLD, 15))
        self.send_button.pack_configure(side=tk.RIGHT, padx=7)

        self.textbox = tk.Text(self.frame, height=2, font=("Helvetica", 20, "bold"), borderwidth=2, relief=tk.SOLID)
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack_configure(side=tk.LEFT, padx=3, pady=3)

        self.root.mainloop()

    def shortcut(self, event):
        if event.keysym == 'Return' and event.state == 0:
            print('h')

            "----TO:DO----"

            self.textbox.delete(1.0, tk.END)

App()