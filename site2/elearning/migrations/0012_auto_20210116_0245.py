# Generated by Django 3.1.3 on 2021-01-15 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0011_quiz'),
    ]

    operations = [
        migrations.AddField(
            model_name='bill',
            name='course_name',
            field=models.TextField(default='No name'),
        ),
        migrations.AddField(
            model_name='bill',
            name='course_price',
            field=models.IntegerField(default=0),
        ),
    ]
