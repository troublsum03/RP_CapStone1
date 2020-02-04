from django.contrib import admin

from .models import Greenery


class GreeneryAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'slug']
    class Meta:
        model = Greenery


admin.site.register(Greenery, GreeneryAdmin)

