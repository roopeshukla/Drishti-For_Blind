import boto3
import os
import time

from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1', endpoint_url = "https://dynamodb.us-east-1.amazonaws.com")
table = dynamodb.Table("Blueberry")
time_start = time.time()
while (time.time() - time_start < 600):
    response = table.query(KeyConditionExpression = Key('berry_id').eq(str('id')))
    for item in response["Items"]:
        f_response = item['message']
        print(f_response)
        if f_response == "SceneImage":
            f_response = "clear"
            table.delete_item(Key = {"berry_id": "id"})
            print(f_response)
            os.system("camera_image.py")
        elif f_response == "TextImage":
            f_response = "clear"
            table.delete_item(Key = {"berry_id": "id"})
            print(f_response)
            os.system("ocrimage_capture.py")
        break