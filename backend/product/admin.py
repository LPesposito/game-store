from django.contrib import admin
from .models import Product, Category, ProductImage

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'active')
    list_filter = ('active', 'categories')
    search_fields = ('title',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug')
    search_fields = ('title', 'slug')
    ordering = ('title',)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'is_cover')