from django.contrib import admin
from .models import Producto


# Register your models here.
#admin.site.register(Producto)
@admin.register(Producto)
class AdminProduct(admin.ModelAdmin):
    list_display = ('id','name','category','description','price',)
    list_filter = ('category',)
