import pika
import sys

connection = pika.BlockingConnection()
channel = connection.channel()


def on_message_callback(ch, method, properties, body):
    print(f"Received {body} on neelima")

channel.queue_declare("neelima")
channel.basic_consume(queue="neelima", on_message_callback=on_message_callback, auto_ack=True)
channel.start_consuming()
