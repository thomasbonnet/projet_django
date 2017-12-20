from django.contrib import admin

# Register your models here.
from .models import Voilier, Navigation

admin.site.register(Voilier)
admin.site.register(Navigation)
