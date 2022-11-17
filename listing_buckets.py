import boto3

client = boto3.client(
    's3',
    aws_access_key_id='AKIAYCI6QZFEMVJVRINF',
    aws_secret_access_key='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',

)
response = client.list_buckets()

for name in response['Buckets']:
    print(name['Name'])
    res = client.get_bucket_location(Bucket=name['Name'])
    print(res['LocationConstraint'])
