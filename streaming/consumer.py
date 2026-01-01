import json

from kafka import KafkaConsumer


from main import process_transaction
from streaming.producer import producer

consumer = KafkaConsumer(
    "transactions",
    bootstrap_servers="localhost:9092",
    value_deserializer= lambda m: json.loads(m.decode("utf-8")),
    auto_offset_reset="earliest",
    enable_auto_commit=True
)

def start_consumer():
    print("Ai agent listening for transactions....")
    for message in consumer:
        transaction = message.value
        print("Received Transaction: ", transaction)

        decision = process_transaction(transaction)
        producer.send("decisions", decision)
        print("Decision produced: ", decision)
