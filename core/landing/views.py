from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render (request, "index.html")

def about(request):
    return render (request, "about.html")

def managed(request):
    return render (request, "managed.html")

def services(request):
    return render (request, "services.html")

def training(request):
    return render (request, "training.html")


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        email_content = f'{name} ({email}) sent the following message: {message}'
        recipient_email = 'tango_services@outlook.ie'

        try:
            send_mail(subject, email_content, email, [recipient_email], fail_silently=False)
            messages.success(request, " Message sent successfully! We will contact you soon.")
        except Exception:
            messages.error(request, " Error sending the email. Please try again.")

        return redirect('/')  # Redirigir siempre a index.html

    return redirect('/')  # Si no es POST, redirigir igual




    
def thanks(request):
    return render(request, "thanks.html", {})


