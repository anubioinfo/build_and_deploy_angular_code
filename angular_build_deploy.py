#!/usr/bin/env python

'''
Importing the required libraries
'''
import os
import subprocess as sp
import paramiko
from scp import SCPClient


'''
SSH credential for doing SCP to remote server
'''
SERVER = '192.168.XX.XX'
user = 'user'
passwd = 'lumini123'
buildFilePath = '/var/www/html/code_directory/'
sourceFilePath = buildFilePath+'dist.zip'
destinationFilePath = '/var/tmp/'
destinationWebRoot = '/var/www/html/test/'


'''
Creating build and zipping it
'''

print("Changing the directory...")
os.chdir(buildFilePath)
print("Creating the angular build....")
sp.call("ng build",shell=True )
print('Creating the zip of build directory');
sp.call("zip -r dist.zip dist",shell=True )
print("Copying the build directory to web root...")


'''
Creating the ssh client for doing SCP to remote server
'''
ssh_client=paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname=SERVER,username=user,password=passwd)

'''
Sending the file to remote server on given path
'''
with SCPClient(ssh_client.get_transport()) as scp:
        scp.put(sourceFilePath, destinationFilePath)


'''
Doing SSH to the remote server, changing directory, extracting zip files and moving it to web root location
'''
ssh_client.exec_command('cd '+destinationFilePath)
ssh_client.exec_command('unzip '+destinationFilePath+'dist.zip -d '+destinationFilePath)
stdin, stdout, stderr =  ssh_client.exec_command('cp -a '+destinationFilePath+'dist/* '+destinationWebRoot)
print("stderr: ", stderr.readlines())
print("pwd: ", stdout.readlines())


'''
Closing the ssh client connection
'''
ssh_client.close()
print("**************************DONE*****************************")
