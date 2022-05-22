import pika, json, os, django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vaccination.settings")
django.setup()

from studentVaccination.models import StudentVaccination

params = pika.URLParameters('amqps://qrwyeqdh:5v6gMmc8Dlv6ciDuWacIPS7Z5YpDWj4U@puffin.rmq2.cloudamqp.com/qrwyeqdh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='vaccination')


def callback(ch, method, properties, body):
    print('Received in vaccination')


channel.basic_consume(queue='vaccination', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()