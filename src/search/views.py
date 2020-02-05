from django.shortcuts import render
from django.views.generic import ListView
from greenery.models import Greenery

class SearchGreeneryView(ListView):
    template_name = "search/view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchGreeneryView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        #SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q]
        if query is not None:
            return Greenery.objects.search(query)
        return Greenery.objects.features()
        # note
        # __icontains = field contions this
        # __iexact = fields is exactly this

        
