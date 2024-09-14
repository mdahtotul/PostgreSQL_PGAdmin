import boto3
from decouple import config
from glob2 import glob
import os
from datetime import datetime

S3_BUCKET_NAME = 'global-db-backup-from-ec2-lightsail-bucket'
AWS_ACCESS_KEY_ID=config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY=config('AWS_SECRET_ACCESS_KEY')


repo_path = os.getcwd()
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
s3 = session.resource('s3')
bucket = s3.Bucket(S3_BUCKET_NAME)
folder_depth=3
root_path = 'postgresql'

now = datetime.now()
current_time = now.strftime("%d %b, %Y (%I:%M:%S %p)")
print("DB Backup started at", current_time)


try:
    for level in range(folder_depth):
        # print(level+1)
        root_path = root_path+'/*'
        files = glob(f"{repo_path}/{root_path}",recursive=True)
        for file in files:
            # print(file)
            if os.path.isfile(file):
                bucket_file_path = file.replace(f"{repo_path}/",'')
                # print(bucket_file_path)
                bucket.upload_file(bucket_file_path, bucket_file_path)
    now = datetime.now()
    current_time = now.strftime("%d %b, %Y (%I:%M:%S %p)")
    print("DB Backup finished at ",current_time)
except Exception as e:
    print("Backup failed with error:",e)
        

