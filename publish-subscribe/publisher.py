import pika
import sys


connection = pika.BlockingConnection()
channel = connection.channel()
exchange_name = 'logs'

content = ' '.join(sys.argv[1:])

channel.exchange_declare('logs', exchange_type='fanout')

channel.basic_publish(exchange_name, routing_key='', body=content)
connection.close()
