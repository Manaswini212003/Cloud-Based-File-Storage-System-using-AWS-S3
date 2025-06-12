import boto3
from botocore.exceptions import NoCredentialsError

# AWS credentials - use environment variables or AWS CLI config in practice
AWS_ACCESS_KEY = 'YOUR_ACCESS_KEY'
AWS_SECRET_KEY = 'YOUR_SECRET_KEY'
BUCKET_NAME = 'my-demo-bucket'

def upload_to_s3(file_name, bucket, object_name=None):
    if object_name is None:
        object_name = file_name

    s3 = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY,
                            aws_secret_access_key=AWS_SECRET_KEY)

    try:
        s3.upload_file(file_name, bucket, object_name)
        print(f"✅ {file_name} uploaded to {bucket}/{object_name}")
        return True
    except FileNotFoundError:
        print("❌ File not found.")
    except NoCredentialsError:
        print("❌ AWS credentials not available.")
    return False

if __name__ == "__main__":
    file_path = input("Enter the full path of the file to upload: ")
    upload_to_s3(file_path, BUCKET_NAME)
