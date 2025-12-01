from django.contrib import admin
from django.utils.safestring import mark_safe
from import_export.admin import ImportExportModelAdmin
from adminsortable2.admin import SortableAdminMixin
from .models import Category, Product, Order, Comment, CustomUser

# Oddiy ro'yxatlar
admin.site.register(Order)
admin.site.register(CustomUser)

# Inline Product
class ProductInline(admin.StackedInline):
    model = Product
    extra = 2

# Category admin
@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ['id', 'name', 'get_products']
    inlines = [ProductInline]

    def get_products(self, obj):
        return obj.product_set.count()
    get_products.short_description = 'All Products'

# Product admin
@admin.register(Product)
class ProductAdmin(SortableAdminMixin, admin.ModelAdmin):
    list_display = ['name', 'price', 'category', 'is_stock', 'get_image']
    list_filter = ['category', 'updated_at']
    search_fields = ['name']

    def is_stock(self, obj):
        return obj.stock > 0
    is_stock.boolean = True
    is_stock.short_description = 'In Stock'

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" width="50" />')
        return "-"
    get_image.short_description = 'Image'

# Comment admin
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'text', 'created_at']
