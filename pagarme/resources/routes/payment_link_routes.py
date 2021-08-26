import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/payment_links'

CANCEL_PAYMENT_LINK = BASE_URL + '/{0}/cancel'

PAYMENT_LINK_BY_ID = BASE_URL + '/{0}'

GET_EVENTS_PAYMENT_LINK = BASE_URL + '/{0}/events'
