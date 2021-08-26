import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/balance/operations'

GET_BALANCE_OPERATIONS_BY = BASE_URL
