import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/plans'

GET_ALL_PLANS = BASE_URL

GET_PLAN_BY = BASE_URL

UPDATE_PLAN = BASE_URL + '/{0}'
