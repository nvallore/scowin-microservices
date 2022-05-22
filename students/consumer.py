import pika, json, os, django
from django.forms.models import model_to_dict

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "students.settings")
django.setup()

from student.models import Student

params = pika.URLParameters('amqps://qrwyeqdh:5v6gMmc8Dlv6ciDuWacIPS7Z5YpDWj4U@puffin.rmq2.cloudamqp.com/qrwyeqdh')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='students')


def callback(ch, method, properties, body):

    print('Received in students')

    if properties.content_type == 'student_vaccinated':
        student_details = json.loads(body)
        student = Student.objects.get(id=student_details.get('student'))
        print(student, 'details')
        student.vaccination = student_details.get('id')
        student.save(update_fields=['vaccination'])
        print(model_to_dict(student))
        print('Student Vaccination updated')


channel.basic_consume(queue='students', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()