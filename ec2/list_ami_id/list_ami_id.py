# -*- coding: utf-8 -*-
import boto3
ec2 = boto3.client('ec2')
request = {
    # AMI検索スピードを早めるため、Ownersの指定は必須。指定しないとかなり遅い。
    "Owners" : [
        'self'
    ]
}
response = ec2.describe_images(**request)

image_ids = [ i['ImageId'] for i in response['Images'] ]
print(image_ids)