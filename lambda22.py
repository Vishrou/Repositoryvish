import json

def lambda_handler(event, context):
    return {
      'body': json.dumps('Hello Netra Rou Rishi This is my first jenkins project')
    }