from django.contrib import admin
from product.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'parent', 'status']
    list_filter = ['title']


class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status']
    list_filter = ['title']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
