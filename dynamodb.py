from __future__ import print_function
import ssl
import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'us-east-1', endpoint_url = "https://dynamodb.us-east-1.amazonaws.com")
table = dynamodb.Table("Sample")
id1 = "TextImage"
id2 = "SceneImage"

def call_aws1(message):
		response = table.update_item(Key = {"id" : id1}, UpdateExpression='SET  command = :val1', ExpressionAttributeValues={
			':val1': message }, ReturnValues="UPDATED_NEW")
		print("Success")
		return 1


def call_aws2(message):
	response = table.update_item(Key={"id": id2}, UpdateExpression='SET  command = :val1', ExpressionAttributeValues={
		':val1': message}, ReturnValues="UPDATED_NEW")
	print("Success")
	return 1


#Main function
def main(id):
	ssl._create_default_https_context = ssl._create_unverified_context
	#Open the output.txt file in the read mode"
	if id == id1 :
		fo = open("google_ocr.txt", "rt")
		try:
			e = call_aws1(str(fo.read()))
		except Exception as e:
			print (e)

	# Close opend file
		fo.close()
	else :
		fo = open("output.txt", "rt")
		try:
			e = call_aws2(str(fo.read()))
		except Exception as e:
			print(e)

		# Close opend file
		fo.close()


if __name__ == "__main__":
	id = input()
	main(id)
