from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Painting, Category


def all_paintings(request):
    """ A view to show all paintings, including sorting and search queries """

    paintings = Painting.objects.all()
    query = None
    categories = None

    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            paintings = paintings.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('paintings'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            paintings = paintings.filter(queries)

    context = {
        'paintings': paintings,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'paintings/paintings.html', context)


def painting_detail(request, painting_id):
    """ A view to show individual painting details """

    painting = get_object_or_404(Painting, pk=painting_id)

    context = {
        'painting': painting,
    }

    return render(request, 'paintings/painting_detail.html', context)
