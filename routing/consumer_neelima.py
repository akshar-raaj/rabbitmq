import pika

connection = pika.BlockingConnection()
channel = connection.channel()


def on_message_callback(ch, method, properties, body):
    print(f"Received {body} on neelima")


channel.exchange_declare("family", exchange_type="direct")
channel.queue_declare("neelima")
channel.queue_bind("neelima", "family", routing_key="neelima")
channel.basic_consume(queue="neelima", on_message_callback=on_message_callback, auto_ack=True)
channel.start_consuming()
