from django.shortcuts import render


def index(request):
    """ A view to return the index page """
    # raise Exception('This is a test error')  # ==> Un-comment for Error 500 test.
    return render(request, 'home/index.html')
