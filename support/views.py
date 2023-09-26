from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from .models import Contact
from .forms import ContactForm


def about(request):
    """ A view to return the index page """

    return render(request, 'support/about.html')


def subscribe(request):
    """ A view to return the subscribe page """

    return render(request, 'support/subscribe.html')


def contact(request):
    """ A view to return the contact page """

    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            user_message = form.cleaned_data['message']
            subject = form.cleaned_data['contact_reason']
            message = render_to_string(
                'support/email_confirmation.txt', {
                    'name': name,
                    'message': user_message
                })

            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = [form.cleaned_data['email']]

            send_mail(
                subject,
                message,
                email_from,
                email_to
            )
            messages.success(request, f'Your message was sent successfuly')
            return redirect(reverse('contact'))

        else:
            messages.error(request, f'An error occured, please try again later')

    context = {
        'form': form,
    }

    return render(request, 'support/contact.html', context)
