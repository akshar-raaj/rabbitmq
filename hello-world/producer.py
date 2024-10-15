import pika
import sys


connection = pika.BlockingConnection()
channel = connection.channel()

channel.queue_declare('hello')
channel.queue_declare('namaste')
content = ' '.join(sys.argv[1:])
for i in range(10):
    numbered_content_hello = f'{i+1}: Hello {content}'
    content_bytes = bytes(numbered_content_hello, encoding='utf-8')
    channel.basic_publish(exchange='', routing_key='hello', body=content_bytes)
    print(f"Published {numbered_content_hello}")
    numbered_content_namaste = f'{i+1}: Namaste {content}'
    channel.basic_publish(exchange='', routing_key='namaste', body=numbered_content_namaste)
    print(f"Published {numbered_content_namaste}")
connection.close()
