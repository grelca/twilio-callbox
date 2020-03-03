from src import config
from twilio.twiml.voice_response import VoiceResponse


def handle() -> VoiceResponse:
    response = VoiceResponse()

    # input code
    response.say('please enter your code or press the pound key to be forwarded')
    response.gather(
        method='GET',
        num_digits=config.gather_digits,
        timeout=config.gather_timeout,
    )

    # fallback for no code entered
    response.say('forwarding call')
    response.dial(number=config.fallback_phone)

    return response
