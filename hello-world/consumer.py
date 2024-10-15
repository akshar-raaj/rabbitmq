import pika
import sys


def on_message_callback(channel, method, properties, body):
    print(f"Received {body.decode('utf-8')}")
    channel.basic_ack(delivery_tag=method.delivery_tag)


def main():
    connection = pika.BlockingConnection()
    channel = connection.channel()
    channel.basic_consume('hello', on_message_callback=on_message_callback, auto_ack=False)
    channel.basic_consume('namaste', on_message_callback=on_message_callback, auto_ack=False)
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupting")
        sys.exit(0)
