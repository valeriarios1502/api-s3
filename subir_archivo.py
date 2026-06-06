import boto3
import base64

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    bucket = event['body']['bucket']
    directorio = event['body']['directorio']
    nombre_archivo = event['body']['nombre_archivo']
    contenido = base64.b64decode(event['body']['contenido'])

    key = f"{directorio}/{nombre_archivo}"
    s3.put_object(Bucket=bucket, Key=key, Body=contenido)

    return {
        'statusCode': 200,
        'mensaje': f'Archivo {nombre_archivo} subido a {bucket}/{directorio}'
    }
