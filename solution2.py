import boto3

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

vpc_id = 'your_vpc_id'
subnet_id = 'your_subnet_id'
instance_count = 10

for i in range(1, instance_count+1):
    # Create EC2 instance
    instance_name = f"myinstance{i}"
    instance = ec2.run_instances(
        ImageId='your_ecs_ami_id',
        InstanceType='t3.micro',
        MaxCount=1,
        MinCount=1,
        SubnetId=subnet_id,
        TagSpecifications=[
            {
                'ResourceType': 'instance',
                'Tags': [
                    {
                        'Key': 'Name',
                        'Value': instance_name
                    }
                ]
            }
        ]
    )
    instance_id = instance['Instances'][0]['InstanceId']
    with open(f"{instance_name}_id.txt", "w") as file:
        file.write(instance_id)

    # Create S3 bucket
    bucket_name = f"{dattajaliparthi}-mys3bucket{i}"
    s3.create_bucket(Bucket=bucket_name)

    # Upload instance ID to S3 bucket
    s3.upload_file(f"{instance_name}_id.txt", bucket_name, f"{instance_name}_id.txt")

    print(f"Instance {instance_name} created with ID {instance_id} and S3 bucket {bucket_name} created.")


Assumptions made:

AWS credentials are properly configured on the machine running the script.
The VPC and subnet are already created and available.
You have permissions to create EC2 instances and S3 buckets.
