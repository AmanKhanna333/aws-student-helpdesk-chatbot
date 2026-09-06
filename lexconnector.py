import boto3
import json

lex_client = boto3.client('lexv2-runtime', region_name='us-east-1')

BOT_ID = "08UGU2RM6B"
BOT_ALIAS_ID = "TSTALIASID"
LOCALE_ID = "en_US"

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        message = body.get('message', '')
        session_id = body.get('sessionId', 'default-session')

        response = lex_client.recognize_text(
            botId=BOT_ID,
            botAliasId=BOT_ALIAS_ID,
            localeId=LOCALE_ID,
            sessionId=session_id,
            text=message
        )

        messages = response.get('messages', [])
        bot_response = messages[0]['content'] if messages else "I am sorry I could not understand that."

        return {
            'statusCode': 200,
            'headers': {
                'Access-Control-Allow-Origin': '*',
                'Access-Control-Allow-Headers': 'Content-Type',
                'Access-Control-Allow-Methods': 'POST, OPTIONS'
            },
            'body': json.dumps({'response': bot_response})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': {'Access-Control-Allow-Origin': '*'},
            'body': json.dumps({'error': str(e)})
        }
