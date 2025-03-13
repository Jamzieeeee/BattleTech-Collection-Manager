from django.contrib import admin
from .models import Catalogue, Collection, PaintScheme

# Register your models here.
admin.site.register(Catalogue)
admin.site.register(Collection)
admin.site.register(PaintScheme)
