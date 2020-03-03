from src import config
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse


def handle(code: str) -> VoiceResponse:
    response = VoiceResponse()

    # check for code validity
    if code not in config.valid_codes:
        if len(code) >= 1:
            response.say('invalid code')
        response.say('forwarding call')
        response.dial(number=config.fallback_phone)
        return response

    # send notification sms
    client = Client(config.account_sid, config.auth_token)
    client.messages.create(
        body='Front door unlocked for {}'.format(config.valid_codes[code]),
        to=config.notification_phone,
        from_=config.twilio_phone,
    )

    # unlock door
    response.play(digits=9, loop=3)

    return response
