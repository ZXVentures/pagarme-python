import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/cards'

GET_ALL_CARDS = BASE_URL

GET_CARD_BY = BASE_URL
