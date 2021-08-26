import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/transfers'

CANCEL_TRANSFER = BASE_URL + '/{0}/cancel'

GET_ALL_TRANSFERS = BASE_URL

GET_TRANSFER_BY = BASE_URL