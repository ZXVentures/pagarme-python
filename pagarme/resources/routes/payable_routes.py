import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/payables'

GET_ALL_PAYABLES = BASE_URL

GET_PAYABLE_BY = BASE_URL
