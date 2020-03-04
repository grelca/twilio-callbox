from . import answer, respond


def lambda_handler(event, context):
    try:
        # TODO: handle existence of Digits more explicitly
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
