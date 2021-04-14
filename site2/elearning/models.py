from django.db import models

# Create your models here.
class Instructor(models.Model):
    inst_id = models.AutoField(primary_key=True)
    inst_name = models.TextField()
    isnt_email = models.EmailField()
    inst_password = models.TextField()
    inst_phno = models.IntegerField()
    inst_exp = models.TextField()

    def __str__(self):
        return self.inst_name

class Admin(models.Model):
    admin_id = models.AutoField(primary_key= True)
    name = models.TextField()
    email = models.EmailField()
    password = models.TextField()

    def __str__(self):
        return self.name

class Learner(models.Model):
    learner_id = models.AutoField(primary_key= True)
    learner_name = models.TextField()
    learner_email = models.EmailField()
    learner_password = models.TextField()
    learner_phno = models.IntegerField()

    def __str__(self):
        return self.learner_name

class Courses(models.Model):
    course_id = models.AutoField(primary_key = True)
    course_name = models.TextField()
    course_content_link = models.TextField()
    course_price = models.IntegerField(default=0)
    course_free = models.BooleanField(default=True)


# class Quiz(models.Model):
#     course_id = models.IntegerField()
#     question = models.TextField()
#     answer = models.TextField()
#     option1 = models.TextField()
#     option2 = models.TextField(default='No option')
#     option3 = models.TextField(default='No option')
#     option4 = models.TextField(default='No option')
#     point = models.IntegerField()

class Bill(models.Model):
    billno = models.AutoField(primary_key=True)
    course_id = models.IntegerField()
    course_name = models.TextField(default='No name')
    course_price = models.IntegerField(default=0)


