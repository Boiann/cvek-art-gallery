from django.shortcuts import render, get_object_or_404
from .models import Painting


def all_paintings(request):
    """ A view to show all paintings, including sorting and search queries """

    paintings = Painting.objects.all()

    context = {
        'paintings': paintings,
    }

    return render(request, 'paintings/paintings.html', context)


def painting_detail(request, painting_id):
    """ A view to show individual painting details """

    painting = get_object_or_404(Painting, pk=painting_id)

    context = {
        'painting': painting,
    }

    return render(request, 'paintings/painting_detail.html', context)
