from django.shortcuts import render
from django.views.generic import View

from .utils import get_client_data, yelp_search


class IndexView(View):
    def get(self, request, *args, **kwargs):
        items = []

        city = None

        while not city:
            ret = get_client_data()
            if ret:
                city = ret['city']

        key = request.GET.get('key', None)
        loc = request.GET.get('loc', None)
        
        location = city

        context = {
            'city' : city,
            'busca' : False
        }

        if loc:
            location = loc
        if key:
            items = yelp_search(keyword=key, location=location)
            
            context = {
                'items' : items,
                'city' : location,
                'busca' : True
            }
        return render(request, 'index.html', context)
