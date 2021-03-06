import os

BASE_URL = f'{os.environ.get("INTEGRATION_PAGARME_URL", "https://pagarme.ze.delivery")}/1/transactions'

CALCULATE_INSTALLMENTS_AMOUNT = BASE_URL + '/calculate_installments_amount'

CAPTURE_TRANSACTION_AFTER = BASE_URL + '/{0}/capture'

GENERATE_CARD_HASH_KEY = BASE_URL + '/card_hash_key'

GET_ALL_TRANSACTIONS = BASE_URL

GET_SPECIFIC_TRANSACTION_BY_ID = BASE_URL + '/{0}'

GET_ALL_PAYABLES_WITH_TRANSACTION_ID = BASE_URL + '/{0}/payables'

GET_ALL_POSTBACKS = BASE_URL + '/{0}/postbacks'

GET_EVENTS_TRANSACTION = BASE_URL + '/{0}/events'

GET_SPECIFIC_PAYABLE = BASE_URL + '/{0}/payables/{1}'

GET_TRANSACTION_BY = BASE_URL

GET_TRANSACTION_OPERATION = BASE_URL + '/{0}/operations'

GET_SPECIFIC_POSTBACK = BASE_URL + '/{0}/postbacks/{1}'

PAY_BOLETO = BASE_URL + '/{0}'

PAY_BOLETO_NOTIFY = BASE_URL + '/{0}/collect_payment'

POSTBACK_REDELIVER = BASE_URL + '/{0}/postbacks/{1}/redeliver'

REFUND_TRANSACTION = BASE_URL + '/{0}/refund'

ANTIFRAUD_ANALYSIS = BASE_URL + '/{0}/antifraud_analyses'
