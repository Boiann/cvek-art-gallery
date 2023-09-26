from django.shortcuts import render


def about(request):
    """ A view to return the index page """

    return render(request, 'support/about.html')


def subscribe(request):
    """ A view to return the subscribe page """

    return render(request, 'support/subscribe.html')
