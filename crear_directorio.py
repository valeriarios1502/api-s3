import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']

    s3.put_object(Bucket=bucket, Key=f"{directorio}/")

    return {
        'statusCode': 200,
        'mensaje': f'Directorio {directorio} creado en bucket {bucket}'
    }
