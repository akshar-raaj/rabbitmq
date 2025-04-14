import sys
import os
from pika import BlockingConnection, ConnectionParameters

DEFAULT_QUEUE = 'hello'
DEFAULT_BODY = 'Hello World'


def get_connection(host='localhost', port=5672):
    parameters = ConnectionParameters(host=host, port=port)
    connection = BlockingConnection(parameters)
    return connection


def publish(exchange: str, queue: str, body: str):
    """
    This method publishes to a queue bound to a direct exchange.
    This will not work reliably with fanout, topic or other exchanges.
    """
    host = os.environ.get('RABBITMQ_HOST', 'localhost')
    connection = get_connection(host)
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    channel.basic_publish(exchange=exchange, routing_key=queue, body=body)
    # Close the connection to ensure the buffer is flushed to the network.
    connection.close()


if __name__ == '__main__':
    body = sys.argv[2] if len(sys.argv) > 2 else DEFAULT_BODY
    queue = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_QUEUE
    publish(exchange='', queue=queue, body=body)
