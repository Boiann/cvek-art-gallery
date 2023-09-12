from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Painting, Category, SubCategory


def all_paintings(request):
    """ A view to show all paintings, including sorting and search queries """

    paintings = Painting.objects.all()
    query = None
    categories = None
    subcategories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                paintings = paintings.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            paintings = paintings.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            paintings = paintings.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'subcategory' in request.GET:
            subcategories = request.GET['subcategory'].split(',')
            paintings = paintings.filter(subcategory__name__in=subcategories)
            subcategories = SubCategory.objects.filter(name__in=subcategories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('paintings'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            paintings = paintings.filter(queries)

    # Get all subcategories
    subcategories = SubCategory.objects.all()

    current_sorting = f'{sort}_{direction}'

    context = {
        'paintings': paintings,
        'search_term': query,
        'current_categories': categories,
        'subcategories': subcategories,  # Include subcategories in the context
        'current_sorting': current_sorting,
    }

    return render(request, 'paintings/paintings.html', context)


def painting_detail(request, painting_id):
    """ A view to show individual painting details """

    painting = get_object_or_404(Painting, pk=painting_id)

    context = {
        'painting': painting,
    }

    return render(request, 'paintings/painting_detail.html', context)
