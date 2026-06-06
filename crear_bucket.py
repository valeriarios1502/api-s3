import boto3

def lambda_handler(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket']

    # Obtener región desde el ARN del contexto
    # arn:aws:lambda:us-east-2:123456789:function:mi-funcion
    region = context.invoked_function_arn.split(':')[3]

    # Proceso
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
        'region':  region,
        'mensaje': f'Bucket "{nombre_bucket}" creado exitosamente'
    }
