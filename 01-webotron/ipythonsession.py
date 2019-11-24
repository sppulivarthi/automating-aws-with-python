# coding: utf-8
import boto3
session = boto3.Session(profile_name='shotty')
s3 = session.resource('s3')
for bucket in s3.buckets.all():
    print(bucket)
    
for bucket in s3.buckets.all():
    print(bucket)
    
new_bucket = s3.create_bucket(Bucket='webotron-boto3')
new_bucket = s3.create_bucket(Bucket='webotron1-boto3', CreateBucketConfiguration={'LocationConstraint': us-east-1))
new_bucket = s3.create_bucket(Bucket='webotron1-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'))
new_bucket = s3.create_bucket(Bucket='webotron1-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='webotron1-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-1'})
new_bucket = s3.create_bucket(Bucket='webotron1-boto3', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
