import pika
import sys

DEFAULT_QUEUE_NAME = 'hello'


def on_message_callback(channel, method, properties, body):
    print(f"Received: {body.decode('utf-8')}")
    channel.basic_ack(delivery_tag=method.delivery_tag)


def get_connection(host='localhost', port=5672):
    parameters = pika.ConnectionParameters(host=host, port=port)
    connection = pika.BlockingConnection(parameters)
    return connection


def consume(queue):
    connection = get_connection()
    channel = connection.channel()
    # Do not auto acknowledge messages. Messages should be acknowledged manually.
    channel.basic_consume(queue, on_message_callback=on_message_callback, auto_ack=False)
    channel.start_consuming()


if __name__ == '__main__':
    queue = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_QUEUE_NAME
    try:
        consume(queue=queue)
    except KeyboardInterrupt:
        print("Interrupting")
        sys.exit(0)
