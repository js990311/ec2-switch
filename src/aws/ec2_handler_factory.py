from botocore.config import Config
import boto3

from src.aws.ec2_handler import Ec2Handler


def ec2_handler_factory(config):
    INSTANCE_ID = config['INSTANCE_ID']
    AWS_ACCESS_KEY_ID = config['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = config['AWS_SECRET_ACCESS_KEY']
    AWS_DEFAULT_REGION = config['AWS_DEFAULT_REGION']
    config = Config(
        region_name=AWS_DEFAULT_REGION
    )
    client = boto3.client('ec2', aws_access_key_id=AWS_ACCESS_KEY_ID, aws_secret_access_key=AWS_SECRET_ACCESS_KEY, config=config)
    return Ec2Handler(client, INSTANCE_ID)