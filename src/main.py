import os
from dotenv import load_dotenv

from src.aws.ec2_handler import Ec2Handler
from src.gui.app_view import AppView

if __name__ == "__main__":
    load_dotenv()  # .env 파일로부터 환경변수 로드
    INSTANCE_ID = os.getenv('INSTANCE_ID')
    handler = Ec2Handler(INSTANCE_ID)
    app = AppView(handler)
    app.mainloop()
