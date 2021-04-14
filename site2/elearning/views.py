from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from elearning.models import Instructor,Admin,Learner,Courses,Bill

# Create your views here.
def home(request):
    return render(request,'home.html')

def login(request):
    valid=True
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = None
        try:
            if Instructor.objects.filter(isnt_email=email).exists:
                user = Instructor.objects.get(isnt_email=email)
                request.session['inst_id'] = user.inst_id
                return render(request,'instructor.html',{'valid':valid})
        except Instructor.DoesNotExist:
            try: 
                if Learner.objects.filter(learner_email=email).exists:
                    user = Learner.objects.get(learner_email=email)
                    request.session['learn_id'] = user.learner_id
                    return render(request,'learner.html',{'valid':valid})
            except Learner.DoesNotExist:
                valid = False
                if Admin.objects.filter(email=email).exists:
                    user = Admin.objects.get(email=email)
                    return render(request,'admin.html',{'valid':valid})
                return render(request,'admin.html')
        if user:
            if user.is_active:
                login(request,user)
                try:
                    Instructor.objects.get(user=user)
                    print('you are Instructor') 
                    return render(request, 'instructor.html')
                except Instructor.DoesNotExist:
                    try:
                        Learner.objects.get(user=user)
                        print('you are learner')
                        return render(request, 'learner.html')
                    except Learner.DoesNotExist:
                        try:
                            Admin.objects.get(user=user)
                            print('you are admin')
                            return render(request, 'admin.html')
                        except:
                            return HttpResponse('Sorry try again later!')
                    finally:
                        return HttpResponse('Logged in ')
                finally:
                    return HttpResponse('Logged in ')
            else:
                return HttpResponse(r"ACCOUNT IS NOT LOGGED IN ")
    return render(request,'home.html')

def inst_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phno = request.POST['phoneNo']
        exp = request.POST['experience']
        Instructor.objects.create(inst_name=name,isnt_email=email,inst_password=password,inst_exp=exp,inst_phno=phno)
        return render(request,'instructor_registration.html')
    else:
        return render(request,'instructor_registration.html')

def learner_register(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        phno = request.POST['phoneNo']
        Learner.objects.create(learner_name=name,learner_email=email,learner_password=password,learner_phno=phno)
        return render(request,'learner_registration.html')
    else:
        return render(request,'learner_registration.html')

def buycourse(request):
    courseObj = Courses.objects.all()
    return render(request,'buycourse.html',{'courses':courseObj})

def modifycourse(request):
    courseObj = Courses.objects.all()
    return render(request,'modifycourse.html',{'courses':courseObj})

def deletecourse(request,course_id):
    Courses.objects.filter(course_id= course_id).delete()
    return HttpResponseRedirect('/modifycourse/')


def payment(request,course_id):
    courseObj = Courses.objects.get(course_id = course_id)
    # # card_name = request.POST['name']
    # card_num = request.POST['card_num']
    # cvv = request.POST['cvv']
    print(courseObj.course_id)
    # learn_id = request.session['learn_id']
    # inst_id = request.session['inst_id']
    Bill.objects.create(course_id=course_id,course_name=courseObj.course_name,course_price=courseObj.course_price)
    return render(request,'payment.html',{'course':courseObj})

def bill(request,course_id):
    courseObj = Courses.objects.get(course_id = course_id)
    billObj = Bill.objects.filter(course_name=courseObj.course_name)
    # learn_id = request.session['learn_id']
    # inst_id = request.session['inst_id']
    return render(request,'bill.html',{'bill':billObj,'course':courseObj})

def viewcourses(request):
    courseObj = Courses.objects.all()
    return render(request, 'viewcourses.html',{'courses':courseObj})

# def viewlink(request,course_id):
#     courseObj = Courses.objects.get(course_id = course_id)
#     link = courseObj.course_content_link
#     return render(request,'viewlink.html',{'courselink' : link})

def freecourses(request):
    courseObj = Courses.objects.all()
    return render(request, 'freecourses.html',{'courses':courseObj})

def uploadcourses(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        link  = request.POST['link']
        if int(price) == 0:
            Courses.objects.create(course_name=name, course_price=price, course_content_link= link,course_free=True)
        else:
            Courses.objects.create(course_name=name, course_price=price, course_content_link= link,course_free=False)
        return render(request, 'uploadcourses.html')
    else : 
        return render(request,'uploadcourses.html')

# def quiz(request, course_id):
#     quizObj = Quiz.objects.filter(course_id=course_id)
#     if request.method == 'POST':
#         question_no = request.POST['id']
#         question = Quiz.objects.get(id = question_no)
#         answer = request.POST['answer']
#         if answer == question.answer:
#             return render(request,'quiz.html',{'questions': question, 'correct': True, 'courseid':course_id })
#         else:
#             return render(request,'quiz.html',{'questions': question, 'correct': 'false', 'courseid':course_id })
#     return render(request,'quiz.html',{'courseid':course_id })


def logout(request):
    return redirect('/home/')
            
