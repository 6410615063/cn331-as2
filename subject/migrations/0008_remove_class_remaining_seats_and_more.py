# Generated by Django 4.2.5 on 2023-09-23 16:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0007_alter_class_max_seats_alter_class_remaining_seats_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='class',
            name='remaining_seats',
        ),
        migrations.RemoveField(
            model_name='class',
            name='total_seats',
        ),
    ]
