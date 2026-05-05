import boto3

sns = boto3.client('sns')

def lambda_handler(event, context):
    print("S3 Event Triggered")

    bucket = event['Records'][0]['s3']['bucket']['name']
    file_name = event['Records'][0]['s3']['object']['key']

    message = "File uploaded: " + file_name + " in bucket: " + bucket

    sns.publish(
        TopicArn='arn:aws:sns:eu-north-1:539262297700:soham-notification',
        Message=message,
        Subject='S3 Upload Notification'
    )

    print("SNS notification sent")

    return {
        'statusCode': 200,
        'body': 'Success'
    }