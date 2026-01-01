from streaming.producer import send_transaction

txn = {
    "transaction_id": "txn_kafka_1",
    "customer_id": "cust_99",
    "amount": 120000,
    "currency": "INR",
    "merchant": "CRYPTO_EXCHANGE",
    "country": "SG"
}

send_transaction(txn)
