# Generated by Django 3.1.3 on 2021-01-15 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0009_auto_20210115_0236'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('billno', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Quiz',
        ),
    ]
