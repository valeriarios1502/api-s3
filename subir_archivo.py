import boto3
import base64

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket  = event['body']['bucket']
    directorio     = event['body']['directorio']
    nombre_archivo = event['body']['nombre_archivo']
    contenido_b64  = event['body']['contenido']

    # Proceso
    s3 = boto3.client('s3')
    contenido = base64.b64decode(contenido_b64)
    s3.put_object(
        Bucket=nombre_bucket,
        Key=ruta_objeto,
        Body=contenido
    )

    return {
        'statusCode': 200,
        'bucket':        nombre_bucket,
        'ruta_objeto':   ruta_objeto,
    }