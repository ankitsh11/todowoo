# Generated by Django 3.1.1 on 2020-11-05 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_userr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='dateCompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
