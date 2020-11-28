import paramiko
from utilities.configurations import *


hostname = getConfig()['AWS']['host']
port = getConfig()['AWS']['port']
username = getConfig()['AWS']['username']
password = getConfig()['AWS']['password']

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(
    hostname=hostname,
    port=port,
    username=username,
    password=password
)

stdin, stdout, stderr = ssh.exec_command("ls -a")
print(stdout.readlines())

#Upload
# stfp = ssh.open_sftp()
# destination_path = "practiceCSV.csv"
# local_path = "utilities/practiceCSV.csv"
# stfp.put(local_path, destination_path) #upload method

stdin.close()

