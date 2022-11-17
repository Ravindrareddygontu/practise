import boto3

client = boto3.client(
    's3',
    aws_access_key_id='AKIAYCI6QZFEMVJVRINF',
    aws_secret_access_key='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',

)
response = client.list_buckets(
