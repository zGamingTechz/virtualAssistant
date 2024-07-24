import concurrent.futures
import customtkinter as ctk
from essential_functions import take_voice_input
import functions


class App:
    def __init__(self):
        functions.greet()

        #---Definitions---
        self.root = ctk.CTk()
        self.root.title("Lisa (Llama 2 7b)")
        self.root.geometry("400x540")

        #---Title---
        self.heading = ctk.CTkLabel(
            self.root,
            text="Lisa 👩🏻‍",
            font=ctk.CTkFont(size=50, weight="bold"),
            text_color="#1F6AA5"
        )
        self.heading.pack(pady=20)

        #---Voice Button---
        self.voice_button = ctk.CTkButton(
            self.root, text="Speak",
            font=ctk.CTkFont(size=50, weight="bold"),
            command=self.start_voice_message_task,
            corner_radius=100,
            width=100,
            height=100,
            anchor="center"
        )
        self.voice_button.pack(pady=65)

        #---Frame for button and textbox---
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(side=ctk.BOTTOM, fill=ctk.X, padx=10, pady=10)

        #---Send Button---
        self.send_button = ctk.CTkButton(
            self.frame,
            text="Send 📩",
            font=ctk.CTkFont(size=15, weight="bold"),
            command=self.start_message_task
        )
        self.send_button.pack(side=ctk.RIGHT, padx=7)

        #---Input Box---
        self.textbox = ctk.CTkTextbox(
            self.frame,
            height=2,
            font=ctk.CTkFont(size=20, weight="bold"),
            border_width=2,
            corner_radius=10
        )
        self.textbox.bind("<KeyPress>", self.shortcut)
        self.textbox.pack(side=ctk.LEFT, padx=3, pady=3, fill=ctk.BOTH, expand=True)

        # ---Output Text---
        self.output_textbox = ctk.CTkTextbox(
            self.root,
            height=4,
            font=ctk.CTkFont(size=20, weight="bold"),
            border_width=2,
            corner_radius=10
        )
        self.output_textbox.pack(side=ctk.BOTTOM, padx=13, pady=3, fill=ctk.BOTH, expand=True)

        # Setup executor for background tasks
        self.executor = concurrent.futures.ThreadPoolExecutor()

        self.root.mainloop()

    #---Enter Shortcut---
    def shortcut(self, event):
        if event.keysym == 'Return' and event.state == 0:
            self.start_message_task()

    def start_message_task(self):
        message = self.textbox.get("1.0", ctk.END).strip()
        if message:
            self.textbox.delete("1.0", ctk.END)
            self.root.after(0, self.run_in_background, self.process_message, message)

    def start_voice_message_task(self):
        self.root.after(0, self.run_in_background, self.process_voice_message)

    def run_in_background(self, func, *args):
        future = self.executor.submit(func, *args)
        future.add_done_callback(lambda f: self.root.after(0, self.update_ui, f.result()))

    @staticmethod
    def process_message(message):
        return functions.lisa_functions(message)

    @staticmethod
    def process_voice_message():
        query = take_voice_input()
        if query:
            return functions.lisa_functions(query)
        return ""

    def update_ui(self, response):
        # Ensure response is a string before inserting
        if isinstance(response, str):
            self.output_textbox.delete("1.0", ctk.END)
            self.output_textbox.insert(ctk.END, response + "\n")
        else:
            print(f"Unexpected response type: {type(response)}")


App()
