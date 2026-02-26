# from django.shortcuts import render,HttpResponse
# from .forms import personalDetailsForm,signupform
from django.shortcuts import render
from django.http import HttpResponse
from .forms import personalDetailsForm
from django.contrib import messages
# from .models import Student
def home(request):
    return render(request, 'task/home.html')

def colleges(request):
    college_list = ["SVEW", "VIT", "BVRICE"]
    return render(request, 'task/colleges.html', {"colleges": college_list})

def students(request):
    student_list = [
        {"name": "koushi", "branch": "IT", "age": 18},
        {"name": "harshini", "branch": "CSE", "age": 18},
        {"name": "bhashini", "branch": "IT", "age": 9},
        {"name": "sanvitha", "branch": "IT", "age": 20},
    ]
    return render(request, 'task/students.html', {"students": student_list})
def address(request):
    return render(request, 'task/address.html')




# def signup(request):
#     if(request.method=="POST"):
#         s=signupform(request.POST)
#         if(s.is_valid()):
#             name=s.cleaned_data['name']
#             password=s.cleaned_data['password']
#             print(name,password)
#         else:
#             s=signupform()
#             print(s.errors)
#     return render(request, 'task/signupform.html', {'form':s})


# def login(request):
#     return render(request, 'task/login.html')

# def loginverification(request):
#     uname=request.POST["username"]
#     if uname=="":
#         print("invalid username")
#         return HttpResponse("invalid username")
#     else:
#         print(uname)
#         return HttpResponse("valid username")
# def personaldetails(request):
#     if request.method == "POST":
#         form = personalDetailsForm(request.POST, request.FILES)
#         if form.is_valid():
#             student = form.save()
#             return render(request, 'task/personaldetails.html', {'form': personalDetailsForm(), 'student': student})
#     else:
#         form = personalDetailsForm()
#     return render(request, 'task/personaldetails.html', {'form': form})


# def signup(request):
#     if request.method == "POST":
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             form.save()
#             print(form.cleaned_data['name'])
#             s1=Student.objects.filter(name=form.cleaned_data).exists()   # 
#             print(s1)          #
#             s1=Student(name=form.cleaned_data['name'])  #these two commands are used to store the data in database aswell 
#             s1.save()
#             if s1:
#                 return HttpResponse("Signup Successful")
#             else:
#                 return HttpResponse("No User Found")
#         else:
#             return HttpResponse("Invalid Form Data")
#     else:
#         form = SignUpForm()

#     return render(request, "app2/SignUpForm.html", {"form": form})