from enum import Enum
class Ec2State(Enum):
    PENDING = 0
    RUNNING = 16
    SHUTTINGDOWN = 32
    TERMINATED = 48
    STOPPING = 64
    STOPPED = 80
