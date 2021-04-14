# Generated by Django 3.1.3 on 2021-01-15 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0010_auto_20210115_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_id', models.IntegerField()),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('option1', models.TextField()),
                ('option2', models.TextField(default='No option')),
                ('option3', models.TextField(default='No option')),
                ('option4', models.TextField(default='No option')),
                ('point', models.IntegerField()),
            ],
        ),
    ]