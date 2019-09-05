from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage
from .forms import ContactForm

# Create your views here.


def contact(request):
    contact_form = ContactForm()

    # Si es un POST, recuperamos los datos del formulario
    if request.method == 'POST':
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            # Enviar el email con la información del formulario y redireccionamos
            email = EmailMessage(
                "La Caffettiera: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["jfbermejo@gmail.com"],
                reply_to=[email]
            )
            try:
                email.send()
                # To do ha ido bien, redireccionamos a OK
                return redirect(reverse('contact') + "?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, 'contact/contact.html', {'form': contact_form})
