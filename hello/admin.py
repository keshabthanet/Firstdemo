from django.contrib import admin
from.models import Image

# Register your models here.
#admin.site.register(Image,ImageAdmin)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']

admin.site.register(Image,ImageAdmin)