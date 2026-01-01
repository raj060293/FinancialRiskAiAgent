from main import process_transaction

txn = {
    "transaction_id": "txn_42",
    "customer_id": "cust_99",
    "amount": 95000,
    "currency": "INR",
    "merchant": "CRYPTO_EXCHANGE",
    "country": "SG"
}

result = process_transaction(txn)
print("\n Final Result = ", result)
