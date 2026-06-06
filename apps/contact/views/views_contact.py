from django.shortcuts import render, redirect
from django.contrib import messages
from apps.contact.forms import ContactForm
from apps.contact.services.contact_service import ContactService


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            ContactService.save_message(form, request)
            messages.success(request, 'Mensaje enviado. Me pondré en contacto contigo pronto.')
            return redirect('contact:success')
        messages.error(request, 'Por favor corrige los errores del formulario.')
    else:
        form = ContactForm()
    return render(request, 'pages/contact.html', {'form': form})


def contact_success(request):
    return render(request, 'pages/contact_success.html')
