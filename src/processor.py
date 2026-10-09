def lambda_handler(event, context):
    """AWS Lambda entry point."""
    record = event.get("Records", [{}])[0]
    file_name = record.get("s3", {}).get("object", {}).get("key", "unknown_file")
    return {"statusCode": 200, "body": f"Successfully processed {file_name}"}
