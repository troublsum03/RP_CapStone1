from django.http import Http404
from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404

from .models import Greenery


class GreeneryFeaturedListView(ListView):
    template_name = "greenery/list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Greenery.objects.all().featured()


class GreeneryFeaturedDetailView(DetailView):
    queryset = Greenery.objects.all().featured()
    template_name = "greenery/featured-detail.html"

    # def get_queryset(self, *args, **kwargs):
    #     request = self.request
    #     return Greenery.objects.featured()


class GreeneryListView(ListView):
    template_name = "greenery/list.html"

    def get_queryset(self, *args, **kwargs ):
        request = self.request
        return Greenery.objects.all()


def greenery_list_view(request):
    queryset = Greenery.objects.all()
    context = {
        'object_list': queryset
    }    
    return render(request, "greenery/list.html", context)


class GreeneryDetailSlugView(DetailView):
    queryset = Greenery.objects.all()
    template_name = "greenery/detail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        #instance = get_object_or_404(Greenery, slug=slug, active=True)
        try:
            instance = Greenery.objects.get(slug=slug, active=True)
        except Greenery.DoesNotExist:
            raise Http404("You Lost Homie..")
        except Greenery.MultipleObjectsReturned:
            qs = Greenery.objects.filter(slug=slug, active=True)
            instance = qs.first()
        except:
            raise Http404("Sad Face how you get here ")
        return instance

class GreeneryDetailView(DetailView):
    template_name = "greenery/detail.html"

    def get_context_data(self, *args, **kwargs):
        context = super(GreeneryDetailView, self).get_context_data(*args, **kwargs)
        print(context)
        return context

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Greenery.objects.get_by_id(pk)
        if instance is None:
            raise Http404("We ain't got it bruh!")
        return instance


def greenery_detail_view(request, pk=None, *args, **kwargs):
    instance = Greenery.objects.get_by_id(pk)
    if instance is None:
        raise Http404("We ain't got it bruh!")
    # qs = Greenery.objects.filter(id=pk)
    # #print(qs)
    # if qs.exists() and qs.count() == 1:  # len(qs)
    #     instance = qs.first()
    # else:
    #     raise Http404("Aint Got What You Looking For Bruh!")

    context = {
        'object': instance
    }
    return render(request, "greenery/list.html", context)

