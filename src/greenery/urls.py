from django.conf.urls import url

from .views import (
    GreeneryListView,
    GreeneryDetailSlugView,
)

urlpatterns = [
    url(r'^$', GreeneryListView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', GreeneryDetailSlugView.as_view()),
]

