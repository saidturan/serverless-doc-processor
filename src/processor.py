import boto3
import urllib.parse

s3_client = boto3.client("s3")

def lambda_handler(event, context):
    record = event.get("Records", [{}])[0]
    bucket = record.get("s3", {}).get("bucket", {}).get("name")
    key = urllib.parse.unquote_plus(record.get("s3", {}).get("object", {}).get("key", "unknown"))

    if not bucket or key == "unknown":
        return {"statusCode": 400, "body": "Invalid S3 event"}

    try:
        response = s3_client.head_object(Bucket=bucket, Key=key)
        file_size = response.get("ContentLength", 0)
        return {"statusCode": 200, "body": f"Successfully processed {key}. Size: {file_size} bytes"}
    except Exception as e:
        return {"statusCode": 500, "body": str(e)}
