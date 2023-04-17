import json
import boto3
import uuid
import os

def handler(event, context):
  dynamodb = boto3.resource('dynamodb',region_name='eu-west-1')
  table = dynamodb.Table(os.environ["STORAGE_DBAWS_NAME"])

  # Insert a new row into the table
  table.put_item(Item={
      'id': str(uuid.uuid4()),
      'name': 'John Doe',
      'age': 30
  })

  return {
      'statusCode': 200,
      'headers': {
          'Access-Control-Allow-Headers': '*',
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
      },
      'body': json.dumps('Hello from your new Amplify Python lambda!')
  }

