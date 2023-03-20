from django.shortcuts import render
from django.http import HttpResponse


from listings.choices import state_choices, bedroom_choices, price_choices
from listings.models import Listing
from realtors.models import Realtor

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings': listings,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'state_choices': state_choices
    }

    return render(request, 'pages/index.html', context)

def about(request):
    # All realtors
    realtors = Realtor.objects.order_by('-hire_date')

    # Realtor of the month
    mvp_realtor = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtor
    }


    return render(request, 'pages/about.html', context)
