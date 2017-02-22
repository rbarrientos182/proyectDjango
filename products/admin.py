from django.contrib import admin
from .models import Producto, Favorite


# Register your models here.
#admin.site.register(Producto)
@admin.register(Producto)
class AdminProduct(admin.ModelAdmin):
    list_display = ('name','category','description','price',)
    list_filter = ('category',)

@admin.register(Favorite)
class AdminFavorite(admin.ModelAdmin):
    list_display = ('user', 'product',)
    list_filter = ('user', 'product',)
