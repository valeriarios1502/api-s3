import boto3
import os

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']

    # Proceso
    region = os.environ['AWS_REGION']
    s3 = boto3.client('s3')

    if region == 'us-east-1':
        s3.create_bucket(Bucket=nombre_bucket)
    else:
        s3.create_bucket(
            Bucket=nombre_bucket,
            CreateBucketConfiguration={'LocationConstraint': region}
        )

    return {
        'statusCode': 200,
        'bucket':  nombre_bucket,
        'region':  region,
        'mensaje': f'Bucket "{nombre_bucket}" creado exitosamente'
    }
