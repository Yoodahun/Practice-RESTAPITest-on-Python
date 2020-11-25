import paramiko
from utilities.configurations import *

ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #public key generate

ssh.connect(hostname=getConfig()['AWS_LINUX']['hostname'],
            port=getConfig()['AWS_LINUX']['port'],
            username=getConfig()['AWS_LINUX']['username'],
            password=getConfig()['AWS_LINUX']['password']
            )

