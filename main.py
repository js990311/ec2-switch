import os
from dotenv import load_dotenv

load_dotenv() # .env 파일로부터 환경변수 로드

AWS_ACCESS_KEY = os.getenv('AWS_ACCESS_KEY')
AWS_SECRET_KEY= os.getenv('AWS_SECRET_KEY')

print(AWS_ACCESS_KEY)
print(AWS_SECRET_KEY)
