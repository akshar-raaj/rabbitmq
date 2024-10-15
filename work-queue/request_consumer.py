import requests
import pika
import sys
import time


def on_message_callback(ch, method, properties, body):
    url = body.decode('utf-8')
    print(f"Making request to {url}")
    if url == 'http://foundationai.com':
        time.sleep(5)
    else:
        time.sleep(1)
    resp = requests.get(url)
    print(f"Status code: {resp.status_code}")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    queue_name = 'url-requests'
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.queue_declare(queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue_name, on_message_callback=on_message_callback, auto_ack=False)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(0)
