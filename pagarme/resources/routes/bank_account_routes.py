import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/bank_accounts'

GET_ALL_BANK_ACCOUNTS = BASE_URL

GET_BANK_ACCOUNTS_BY = BASE_URL
