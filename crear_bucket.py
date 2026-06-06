import boto3
import os

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']

    # Proceso
    region = os.environ.get('AWS_REGION') or os.environ.get('AWS_DEFAULT_REGION')
    s3 = boto3.client('s3', region_name=region)

    if region == 'us-east-1':
        s3.create_bucket(Bucket=nombre_bucket)
    else:
        s3.create_bucket(
            Bucket=nombre_bucket,
            CreateBucketConfiguration={'LocationConstraint': region}
        )

    return {
        'statusCode': 201,
        'bucket':  nombre_bucket,
    }
