import pika, json

params = pika.URLParameters('amqps://qrwyeqdh:5v6gMmc8Dlv6ciDuWacIPS7Z5YpDWj4U@puffin.rmq2.cloudamqp.com/qrwyeqdh')

connection = pika.BlockingConnection(params)

channel = connection.channel()


def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='vaccination', body=json.dumps(body), properties=properties)
