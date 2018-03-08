# build_and_deploy_angular_code
Python code to build angular code on local machine and deploy it to remote server.
You have to do following to run this python script
1) Install python3
2) Open the script file and set following:
    SERVER = '192.168.XX.XX'
    user = 'user'
    passwd = 'lumini123'
    buildFilePath = '/var/www/html/code_directory/'
    sourceFilePath = buildFilePath+'dist.zip'
    destinationFilePath = '/var/tmp/'
    destinationWebRoot = '/var/www/html/test/'
3) execute the script by running following command:
    python3 angular_build_deploy.py
