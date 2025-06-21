import tkinter as tk
from tkinter import font as tkfont

class AppView(tk.Tk):
    def __init__(self, ec2_handler):
        super().__init__()
        self.ec2_handler = ec2_handler

        self.title("EC2 MANAGEr")
        self.geometry("1600x900")
        self.status_font = tkfont.Font(family="Arial", size=20, weight="bold")

        # 인스턴스 상태창 배치
        self.status_label = tk.Label(self, text="[INIT]", font=self.status_font)
        self.status_label.pack(pady=30)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        self.status_button = tk.Button(button_frame, text="Check Status", command=self.get_state)
        self.status_button.pack(side="left", pady=5)

    def get_state(self):
        self.status_label.config(text="Checking Now", fg="black")
        try:
            state = self.ec2_handler.get_state()
            self.status_label.config(text=f"Instance Status = {state.name}", fg="black")
        except Exception as e:
            self.handle_error(e)

    def handle_error(self, e):
        self.status_label.config(text=f"EXCEPTION RAISE : {str(e)}", fg="red")

