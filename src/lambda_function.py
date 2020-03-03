from src import answer, respond


def lambda_handler(event, context):
    try:
        response = respond.handle(event['queryStringParameters']['Digits'])
    except:
        response = answer.handle()

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/xml'
        },
        'body': response.to_xml()
    }
