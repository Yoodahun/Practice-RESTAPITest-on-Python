import paramiko
import csv
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

stdin, stdout, stderr = ssh.exec_command("python3 HelloWorld.py")
print(stdout.readlines())

#Upload
stfp = ssh.open_sftp()
destination_path = "practiceCSV.csv"
local_path = "utilities/practiceCSV.csv"
stfp.put(local_path, destination_path) #upload method

#Trigger the batch Command?
stdin, stdout, stderr = ssh.exec_command("python script.py")

#Download the file to local folder
stfp.get("demofile", "SSHExample/downloadedFile/demofile.txt")

#Parse output file csv
# with open("~~") as csvFile:
#     csv_reader = csv.reader(csvFile, delimiter=',')
#     for row in csv_reader:
#         if row[0] == "~~":
#             assert row[1] == "rejected"

stdin.close()

