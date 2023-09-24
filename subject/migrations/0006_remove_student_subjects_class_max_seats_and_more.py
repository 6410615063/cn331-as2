# Generated by Django 4.2.5 on 2023-09-23 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0005_remove_subject_description_alter_class_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='subjects',
        ),
        migrations.AddField(
            model_name='class',
            name='max_seats',
            field=models.PositiveIntegerField(default=99, editable=False),
        ),
        migrations.AlterField(
            model_name='class',
            name='remaining_seats',
            field=models.PositiveIntegerField(default=99, editable=False),
        ),
        migrations.AlterField(
            model_name='class',
            name='total_seats',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
    ]
