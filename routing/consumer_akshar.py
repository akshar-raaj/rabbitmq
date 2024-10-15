import pika

connection = pika.BlockingConnection()
channel = connection.channel()


def on_message_callback(ch, method, properties, body):
    print(f"Received {body} on akshar")


channel.queue_declare("akshar")
channel.basic_consume(queue="akshar", on_message_callback=on_message_callback, auto_ack=True)
channel.start_consuming()
