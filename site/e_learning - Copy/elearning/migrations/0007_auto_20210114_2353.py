# Generated by Django 3.1.3 on 2021-01-14 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elearning', '0006_courses_course_free'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_free',
            field=models.BooleanField(),
        ),
    ]
