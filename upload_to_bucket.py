import boto3

filename: str = "exchange_rate.png"
bucketname: str = "shaglibucket"

s3 = boto3.client("s3")
s3.upload_file(filename, bucketname, filename)
