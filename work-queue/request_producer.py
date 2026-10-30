import pika
import sys

# Publish the URLs given on the command line, or 10 alternating default URLs.
urls = sys.argv[1:] or ['http://agiliq.com', 'http://foundationai.com'] * 5

connection = pika.BlockingConnection()
channel = connection.channel()
queue_name = 'url-requests'
channel.queue_declare(queue_name, durable=True)
# With confirms enabled, basic_publish blocks until the broker accepts the message, and raises if it does not.
channel.confirm_delivery()
for url in urls:
    channel.basic_publish(exchange='', routing_key=queue_name, body=url, properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))
    print(f"Published {url}")
connection.close()
