import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/customers'

GET_ALL_CUSTOMERS = BASE_URL

GET_CUSTOMER_BY = BASE_URL
