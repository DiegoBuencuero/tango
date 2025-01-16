from django.shortcuts import render, redirect
from django.core.mail import send_mail

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
        # Obtener los datos del formulario
        nombre = request.POST.get('nombre', '')
        correo = request.POST.get('correo', '')
        asunto = request.POST.get('asunto', '')  # Aquí corregimos el nombre del campo
        mensaje = request.POST.get('mensaje', '')

        # Construir el texto del mensaje
        texto = f'{nombre} ({correo}) enviou a seguinte mensagem: {mensaje}'

        # Dirección de correo a donde enviar el mensaje
        correo_destino = 'dratainakoster@gmail.com'

        # Envía el correo electrónico
        send_mail(
            asunto,
            texto,
            correo,
            [correo_destino],
            fail_silently=False,        )

        return redirect('thanks')  # Redirige a la página de agradecimiento

    else:
        # Si no es una solicitud POST, simplemente renderiza el formulario
        return render(request, 'contact.html', {})
    
def thanks(request):
    return render(request, "thanks.html", {})


