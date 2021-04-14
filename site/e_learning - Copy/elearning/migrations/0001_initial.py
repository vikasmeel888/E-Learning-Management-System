# Generated by Django 3.1.3 on 2021-01-12 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('password', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.TextField()),
                ('course_content_link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('inst_id', models.AutoField(primary_key=True, serialize=False)),
                ('inst_name', models.TextField()),
                ('isnt_email', models.EmailField(max_length=254)),
                ('inst_password', models.TextField()),
                ('inst_phno', models.IntegerField(max_length=10)),
                ('inst_exp', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Learner',
            fields=[
                ('leanrner_id', models.AutoField(primary_key=True, serialize=False)),
                ('learner_name', models.TextField()),
                ('learner_email', models.EmailField(max_length=254)),
                ('learner_password', models.TextField()),
                ('learner_phno', models.IntegerField(max_length=10)),
                ('courses_enrolled', models.TextField()),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('answer', models.TextField()),
                ('options', models.TextField()),
                ('point', models.IntegerField()),
            ],
        ),
    ]
