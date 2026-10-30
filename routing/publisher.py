import pika
import sys

if len(sys.argv) < 3:
    sys.exit("Usage: python publisher.py <akshar|neelima> <message>")

routing_key = sys.argv[1]
body = ' '.join(sys.argv[2:])

connection = pika.BlockingConnection()
channel = connection.channel()

channel.exchange_declare('family', exchange_type='direct')

# Declare and bind both queues so messages published before a consumer starts are kept.
for queue in ('akshar', 'neelima'):
    channel.queue_declare(queue)
    channel.queue_bind(queue, 'family', routing_key=queue)

channel.basic_publish('family', routing_key=routing_key, body=body)
connection.close()
