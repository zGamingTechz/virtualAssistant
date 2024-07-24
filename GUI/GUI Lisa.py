import customtkinter as ctk


class App:
    def __init__(self):
        #---Definitions---
        self.root = ctk.CTk()
        self.root.title("Lisa (Llama 2 7b)")
        self.root.geometry("400x540")

        #---Layout---
        self.heading = ctk.CTkLabel(
            self.root,
            text="Lisa 👩🏻‍",
            font=ctk.CTkFont(size=50, weight="bold"),
            text_color="#1F6AA5"
        )
        self.heading.pack(pady=20)

        # Create a circular button
        self.voice_button = ctk.CTkButton(
            self.root, text="Speak",
            font=ctk.CTkFont(size=50, weight="bold"),
            command=self.send_message,
            corner_radius=100,
            width=100,
            height=100,
            anchor="center"
        )
        self.voice_button.pack(pady=100)

        # Frame for button and textbox
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(side=ctk.BOTTOM, fill=ctk.X, padx=10, pady=10)

        self.send_button = ctk.CTkButton(
            self.frame,
            text="Send 📩",
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.send_message
        )
        self.send_button.pack(side=ctk.RIGHT, padx=7)

        self.textbox = ctk.CTkTextbox(
            self.frame,
            height=2,
            font=ctk.CTkFont(size=20, weight="bold"),
            border_width=2,
            corner_radius=10
        )
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(side=ctk.LEFT, padx=3, pady=3, fill=ctk.BOTH, expand=True)

        self.root.mainloop()

    def shortcut(self, event):
        if event.keysym == 'Return' and event.state == 0:
            self.send_message()

    def send_message(self):
        message = self.textbox.get("1.0", ctk.END)
        print(message)
        "----TO:DO----"
        # ai_chat.chat()

        self.textbox.delete("1.0", ctk.END)


App()