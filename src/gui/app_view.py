import tkinter as tk
from tkinter import font as tkfont

class AppView(tk.Tk):
    def __init__(self, ec2_handler):
        super().__init__()
        self.ec2_handler = ec2_handler

        self.title("EC2 MANAGEr")
        self.geometry("1600x900")
        self.status_font = tkfont.Font(family="Arial", size=20, weight="bold")

        # 버튼
        button_frame = tk.Frame(self)
        button_frame.pack(pady=10)

        # 상태 보기 버튼
        self.status_button = tk.Button(button_frame, text="Check Status", command=self.get_state)
        self.status_button.pack(side="left", pady=5)

        # 시작 버튼
        self.start_button = tk.Button(button_frame, text="Start Instance", command=self.start_instance)
        self.start_button.pack(side="left", pady=5)

        # 정지 버튼
        self.stop_button = tk.Button(button_frame, text="Stop Instance", command=self.stop_instance)
        self.stop_button.pack(side="left", pady=5)


        # 인스턴스 상태창
        text_frame = tk.Frame(self)
        text_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Text
        self.status_text = tk.Text(
            text_frame,
            height=40,  # 보여줄 라인 수
            wrap="word", # 단어 단위로 자동 줄바꿈
            font=("Consolas", 12), # 고정폭 글꼴이 가독성에 좋음
            state="disabled" # 기본적으로 읽기 전용으로 설정
        )
        self.status_text.pack(side="left", fill="both", expand=True)

        # Scrollbar
        scrollbar = tk.Scrollbar(text_frame, command=self.status_text.yview)
        scrollbar.pack(side="right", fill="y")
        self.status_text.config(yscrollcommand=scrollbar.set)

    def update_status_text(self, text, tag="DEFAULT"):
        self.status_text.config(state="normal") # 내용 수정을 위헤
        self.status_text.delete("1.0", tk.END) # 기존내용 삭제
        self.status_text.insert(tk.END, text, tag) # 내용 삽입
        self.status_text.config(state="disabled") # 읽기모드
        self.update_idletasks()

    def get_state(self):
        self.update_status_text(text="Checking Now")
        try:
            state = self.ec2_handler.get_state()
            self.update_status_text(text=f"Instance Status = {state.name}")
        except Exception as e:
            self.handle_error(e)

    def start_instance(self):
        self.update_status_text(text="Try To Start Instance")
        try:
            isStart = self.ec2_handler.start_instance()
            if isStart:
                self.update_status_text(text="Start Instance. Check state")
            else:
                self.update_status_text(text="Instance is Already Started")
        except Exception as e:
            self.handle_error(e)

    def stop_instance(self):
        self.update_status_text(text="Try To Start Instance")
        try:
            isStop = self.ec2_handler.stop_instance()
            if isStop:
                self.update_status_text(text="Stop Instance. Check state")
            else:
                self.update_status_text(text="Instance is Already Stopped")
        except Exception as e:
            self.handle_error(e)


    def handle_error(self, e):
        self.update_status_text(text=f"EXCEPTION RAISE : {str(e)}", tag="WARN")

