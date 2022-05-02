from django.shortcuts import render, redirect
from .models import Contact

from django.core.mail import send_mail


def home_view(request):
    if request.method == "POST":
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        message = request.POST.get('message')

        Contact.objects.create(
            fullname=fullname, email=email, contact=contact, message=message)

        send_mail(
            subject=f"Message Sent From {fullname}, Email {email}",
            message=message,
            from_email='dummy@email.com',
            recipient_list=['khyalthatta2@gmail.com'],
            fail_silently=True
        )
        return redirect('home')
    return render(request, 'blog/index.html')


def contact_view(request):
    context = {
        'infos': Contact.objects.all()
    }

    return render(request, 'blog/info.html', context=context)
