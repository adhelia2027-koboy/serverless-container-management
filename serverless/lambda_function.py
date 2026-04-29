import json
 
 
def lambda_handler(event, context):
    query_params = event.get("queryStringParameters") or {}
    name = query_params.get("name", "Cloud Engineer")
 
    response_body = {
        "message": f"Hello, {name}!"
    }
 
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps(response_body)
    }
