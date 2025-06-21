import os

from enum import Enum
from botocore.exceptions import ClientError
from dotenv import load_dotenv
import boto3

from exceptions import DryRunFailException, Ec2ClientException


class Ec2State(Enum):
    PENDING = 0
    RUNNING = 16
    SHUTTINGDOWN = 32
    TERMINATED = 48
    STOPPING = 64
    STOPPED = 80

load_dotenv() # .env 파일로부터 환경변수 로드

def get_state(client, instance_id):
    try:
        response = client.describe_instances(InstanceIds=[instance_id], DryRun=True)
    except ClientError as e:
        if 'DryRunOperation' not in str(e):
            raise DryRunFailException(str(e))
    except Exception as e:
        raise RuntimeError(str(e))
    try:
        response = client.describe_instances(InstanceIds=[instance_id])
        """
            0 : Pending
            16 : running
            32 : shutting-down
            48 : Termnated
            64 : Stopping
            80 : Stopped
        """
        return Ec2State(response['Reservations'][0]['Instances'][0]['State']['Code'])
    except ClientError as e:
        raise Ec2ClientException(str(e))

if __name__ == '__main__':
    INSTANCE_ID = os.getenv('INSTANCE_ID')
    ec2 = boto3.client('ec2')
    state = get_state(ec2, INSTANCE_ID)
    print(f"state = {state.name} steate value = {state.value}")
