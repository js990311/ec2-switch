import os
from dotenv import load_dotenv
import boto3

load_dotenv() # .env 파일로부터 환경변수 로드

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY= os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_DEFAULT_REGION = os.getenv('AWS_DEFAULT_REGION')

print(AWS_ACCESS_KEY_ID)
print(AWS_SECRET_ACCESS_KEY)
print(AWS_DEFAULT_REGION)

ec2 = boto3.client('ec2')
response = ec2.describe_instances()
print(response)
