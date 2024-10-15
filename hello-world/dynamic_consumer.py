import pika
import sys

connection = pika.BlockingConnection()
channel = connection.channel()

auto_ack = True if len(sys.argv) > 2 else False

def on_message_callback(ch, method, properties, body):
    print(body)
    if auto_ack is False:
        ch.basic_ack(delivery_tag=method.delivery_tag)


queue_name = sys.argv[1]
channel.queue_declare(queue_name)
channel.basic_consume(queue=queue_name, on_message_callback=on_message_callback, auto_ack=auto_ack)
channel.start_consuming()
