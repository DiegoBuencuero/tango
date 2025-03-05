from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages

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
        # Get form data
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

        # Build the email content
        email_content = f'{name} ({email}) sent the following message: {message}'

        # Destination email address
        recipient_email = 'tango_services@outlook.ie'

        try:
            # Send email
            send_mail(subject, email_content, email, [recipient_email], fail_silently=False)

            # Add success message
            messages.success(request, "Message sent successfully! We will contact you soon.")
        except Exception:
            messages.error(request, "Error sending the email. Please try again.")

        return redirect('contact')  # Redirect to reload the form and show the message

    return render(request, 'index.html')


    
def thanks(request):
    return render(request, "thanks.html", {})


