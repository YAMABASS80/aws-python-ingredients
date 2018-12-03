# -*- coding: utf-8 -*-
import boto3
ec2 = boto3.client('ec2')
response = ec2.describe_instances()

reservations = []
for r in response['Reservations']:
    reservations.append(r)

instances = []
for i in reservations:
    instances.extend(i['Instances'])

instance_ids = []
for i in instances:
    instance_ids.append(i['InstanceId'])

print(instance_ids)