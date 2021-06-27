import json
import requests
import boto3

def lambda_handler(event, context):
    try:
        ec2client = boto3.client('ec2')
        response = ec2client.describe_instances()
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                # This sample print will output entire Dictionary object
                #print(instance)
                # This will print will output the value of the Dictionary key 'InstanceId'
                print(instance["InstanceId"])
    except requests.RequestException as e:
            # Send some context about this error to Lambda Logs
            print(e)
            raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            #"location": ip.text.replace("\n", "")
        }),
    }
