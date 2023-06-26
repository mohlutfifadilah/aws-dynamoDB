import boto3
s3_client = boto3.client("s3")
dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("profile")

def lambda_handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    resp = s3_client.get_object(Bucket=bucket_name,Key=s3_file_name)
    data = resp['Body'].read().decode("utf-8")
    Students = data.split("\n")
    #print(friends)
    for friend in Students:
        print(friend)
        friend_data = friend.split(";")
        # add to dynamodb
        try:
            table.put_item(
                Item = {
                    "nim"       : friend_data[0],
                    "nama"      : friend_data[1]
                }
            )
        except Exception as e:
            print("e")
