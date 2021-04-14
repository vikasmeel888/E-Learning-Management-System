from django.contrib import admin

# Register your models here.
from elearning.models import * 
# Register your models here.
admin.site.register(Admin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Courses)
admin.site.register(Bill)
