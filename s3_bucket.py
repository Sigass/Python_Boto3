import boto3
from botocore.exceptions import ClientError

# 1. Initialisation
s3 = boto3.client('s3', region_name='us-west-2')
bucket_name = 'mon-unique-bucket-sigass-2026' # Doit être unique au MONDE

try:
    print(f"Création du bucket : {bucket_name}...")
    
    # 2. Création du bucket
    # Note : Pour toutes les régions sauf us-east-1, il FAUT spécifier LocationConstraint
    s3.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            'LocationConstraint': 'us-west-2'
        }
    )
    
    print("Succès ! Le bucket est prêt.")

except ClientError as e:
    print(f"Erreur lors de la création : {e}")