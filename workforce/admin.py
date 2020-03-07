from django.contrib import admin
from workforce.models import Clown


class ClownAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'description', 'slug', )


admin.site.register(Clown, ClownAdmin)
