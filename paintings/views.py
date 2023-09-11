from django.shortcuts import render
from .models import Painting


def all_paintings(request):
    """ A view to show all paintings, including sorting and search queries """

    paintings = Painting.objects.all()

    context = {
        'paintings': paintings,
    }

    return render(request, 'paintings/paintings.html', context)
