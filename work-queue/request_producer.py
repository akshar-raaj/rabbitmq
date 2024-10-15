import pika
import sys

connection = pika.BlockingConnection()
channel = connection.channel()
queue_name = 'url-requests'
channel.queue_declare(queue_name, durable=True)
url = sys.argv[1]
urls = ['http://agiliq.com', 'http://foundationai.com']
for i in range(10):
    url = urls[i%2]
    channel.basic_publish(exchange='', routing_key=queue_name, body=url, properties=pika.BasicProperties(delivery_mode=pika.DeliveryMode.Persistent))
    print(f"Published {url}")
