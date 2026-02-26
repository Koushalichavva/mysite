from django.shortcuts import render,HttpResponse
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,   # from email
            ['chavvakoushali@gmail.com'],    # to email (can be same)
            fail_silently=False,
        )

        return HttpResponse("Email sent successfully!")

    return render(request, 'contact/contact.html')

