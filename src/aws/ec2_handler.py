import os

from botocore.exceptions import ClientError
from dotenv import load_dotenv
import boto3
from src.aws.ec2_state import Ec2State
from src.aws.exceptions import DryRunFailException, Ec2ClientException

class Ec2Handler:
    def __init__(self, client, instance_id):
        self.client = client
        self.instace_id = instance_id

    def get_state(self):
        try:
            response = self.client.describe_instances(InstanceIds=[self.instace_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise DryRunFailException(str(e))
        except Exception as e:
            raise RuntimeError(str(e))
        try:
            response = self.client.describe_instances(InstanceIds=[self.instace_id])
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

    def start_instance(self):
        state = None
        try:
            state = self.get_state()
        except Exception as e:
            raise e
        try:
            self.ec2.start_instances(InstanceIds=[self.instace_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise DryRunFailException(str(e))
        except Exception as e:
            raise RuntimeError(str(e))

        if (state == Ec2State.RUNNING or state == Ec2State.PENDING):
            return False
        try:
            self.ec2.start_instances(InstanceIds=[self.instace_id], DryRun=False)
            return True
        except Exception as e:
            raise Ec2ClientException(str(e))

    def stop_instance(self):
        state = None
        try:
            state = self.get_state()
        except Exception as e:
            raise e
        try:
            self.client.stop_instances(InstanceIds=[self.instace_id], DryRun=True)
        except ClientError as e:
            if 'DryRunOperation' not in str(e):
                raise DryRunFailException(str(e))
        except Exception as e:
            raise RuntimeError(str(e))

        if(state == Ec2State.STOPPED or state == Ec2State.STOPPING):
            return False
        try:
            self.client.stop_instances(InstanceIds=[self.instace_id], DryRun=False)
            return True
        except Exception as e:
            raise Ec2ClientException(str(e))

if __name__ == "__main__":
    load_dotenv()  # .env 파일로부터 환경변수 로드
    INSTANCE_ID = os.getenv('INSTANCE_ID')
    handler = Ec2Handler(INSTANCE_ID)
    state = handler.get_state()
    print(state)
