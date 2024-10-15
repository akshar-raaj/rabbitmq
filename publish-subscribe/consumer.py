import pika


def on_message_callback(ch, method, properties, body):
    print("Received message")
    print(body)


def main():
    connection = pika.BlockingConnection()
    exchange_name = 'logs'
    channel = connection.channel()
    channel.exchange_declare(exchange_name, exchange_type='fanout')
    result = channel.queue_declare('', exclusive=True)
    queue_name = result.method.queue
    channel.queue_bind(queue_name, exchange=exchange_name)
    channel.basic_consume(queue_name, on_message_callback=on_message_callback, auto_ack=False)
    channel.start_consuming()


main()