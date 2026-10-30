import pika

connection = pika.BlockingConnection()
channel = connection.channel()


def on_message_callback(ch, method, properties, body):
    print(f"Received {body} on akshar")


channel.exchange_declare("family", exchange_type="direct")
channel.queue_declare("akshar")
channel.queue_bind("akshar", "family", routing_key="akshar")
channel.basic_consume(queue="akshar", on_message_callback=on_message_callback, auto_ack=True)
channel.start_consuming()
