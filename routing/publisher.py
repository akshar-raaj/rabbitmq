import pika


connection = pika.BlockingConnection()
channel = connection.channel()

channel.exchange_declare('family', exchange_type='direct')

channel.queue_declare('akshar')
channel.queue_bind('akshar', 'family', routing_key='akshar')

channel.queue_declare('neelima')
# Probably the same routing_key as the queue_name is used while binding to a direct exchange.
channel.queue_bind('neelima', 'family')
