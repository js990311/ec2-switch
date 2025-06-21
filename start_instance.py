import os

from botocore.exceptions import ClientError
from dotenv import load_dotenv
import boto3

from exceptions import DryRunFailException, Ec2ClientException
from get_state import get_state, Ec2State

load_dotenv() # .env 파일로부터 환경변수 로드

def start_instance(client, instance_id):
    state = None
    try:
        state = get_state(client, instance_id)
    except Exception as e:
        raise e
    try:
        client.start_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise DryRunFailException(str(e))
    except Exception as e:
        raise RuntimeError(str(e))

    if(state == Ec2State.RUNNING or state == Ec2State.PENDING):
        return False
    try:
        client.start_instances(InstanceIds=[instance_id], DryRun=False)
        return True
    except Exception as e:
        raise Ec2ClientException(str(e))

if __name__ == "__main__":
    INSTANCE_ID = os.getenv('INSTANCE_ID')
    ec2 = boto3.client('ec2')
    isStart = start_instance(ec2, INSTANCE_ID)
    if isStart:
        print("On")
    else:
        print("Aleady running")
