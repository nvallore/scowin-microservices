# Generated by Django 4.0.2 on 2022-05-21 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_student_vaccination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(max_length=4, primary_key=True, serialize=False),
        ),
    ]