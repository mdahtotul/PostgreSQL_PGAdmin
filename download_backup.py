import boto3
from decouple import config
import os

S3_BUCKET_NAME = 'global-db-backup-from-ec2-lightsail-bucket'
AWS_ACCESS_KEY_ID = config('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')

folders = ['pg_notify', 'pg_replslot', 'pg_stat', 'pg_tblspc', 'pg_twophase',
           'pg_snapshots', 'pg_logical/snapshots', 'pg_logical/mappings', 'pg_commit_ts']

session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)
s3 = session.resource('s3')
bucket = s3.Bucket(S3_BUCKET_NAME)

root_path = 'postgresql/data'

for obj in bucket.objects.filter(Prefix='postgresql'):
    if not os.path.exists(os.path.dirname(obj.key)):
        os.makedirs(os.path.dirname(obj.key))
    print(obj.key)
    bucket.download_file(obj.key, obj.key)  # save to same path

for folder in folders:
    if not os.path.exists(f'{root_path}/{folder}'):
        os.mkdir(f'{root_path}/{folder}')
