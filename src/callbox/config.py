import json
from os import getenv

# twilio configs
account_sid = getenv('ACCOUNT_SID', '')
auth_token = getenv('AUTH_TOKEN', '')

# gather configs
gather_digits = getenv('GATHER_DIGITS', 4)
gather_timeout = getenv('GATHER_TIMEOUT', 10)

# validation configs
valid_codes = json.loads(getenv('VALID_CODES', '{"1234":"test"}'))

# phone numbers
fallback_phone = getenv('FALLBACK_PHONE', '+15005550006')
notification_phone = getenv('NOTIFICATION_PHONE', fallback_phone)
twilio_phone = getenv('TWILIO_PHONE', '+15005550006')
