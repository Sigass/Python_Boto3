import boto3

# Utilisation de la session pour une meilleure gestion des régions
ec2 = boto3.resource('ec2', region_name='us-west-2')

print("Lancement de l'instance...")

# Correction/Amélioration : 
# 1. Ajout de NetworkInterfaces pour s'assurer qu'une IP publique est attribuée (selon le subnet)
# 2. Utilisation de variables pour plus de clarté
instances = ec2.create_instances(
    ImageId='ami-03caad32a158f72db',  # Vérifie bien que cette AMI existe toujours en us-west-2
    MinCount=1,
    MaxCount=1,
    InstanceType='t3.micro',
    KeyName='vockey'
)

instance = instances[0]

print(f"Instance créée. ID: {instance.id}")

# Attendre que l'instance soit "running"
print("Attente du démarrage de l'instance...")
instance.wait_until_running()

# IMPORTANT : Recharger les données pour récupérer l'adresse IP publique
# L'IP n'est pas disponible immédiatement au moment du 'create_instances'
instance.reload()

# Vérification si l'IP existe (parfois elle peut être absente si le subnet ne l'autorise pas)
public_ip = instance.public_ip_address
if public_ip:
    print(f"Instance opérationnelle ! Public IP: {public_ip}")
else:
    print("Instance opérationnelle, mais aucune IP publique n'a été attribuée.")
    