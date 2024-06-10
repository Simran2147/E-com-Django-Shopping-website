from django.contrib import admin
from .models import Category, Product
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name','slug']
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
        list_display = ['nameProd', 'slug', 'price','created_at', 'updated_at', 'stock','available', 'Category']
        list_filter = ['available', 'updated_at', 'created_at']
        list_editable = ['price','stock','available']
        prepopulated_fields = {'slug': ('nameProd',)}



admin.site.register(Product, ProductAdmin)


