from django.conf.urls import url

from .views import (
    SearchGreeneryView
)

app_name = "search"

urlpatterns = [
    url(r'^$', SearchGreeneryView.as_view(), name='query'),
]
