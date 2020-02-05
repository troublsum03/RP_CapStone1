from django.conf.urls import url

from .views import (
    GreeneryListView,
    GreeneryDetailSlugView,
)

app_name = "greenery"

urlpatterns = [
    url(r'^$', GreeneryListView.as_view(), name='list'),
    url(r'^(?P<slug>[\w-]+)/$', GreeneryDetailSlugView.as_view(), name='detail'),
]

