from django.contrib import admin
from apps.main.models import Page, ProductSet
from adminsortable2.admin import SortableAdminMixin


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


class ProductSetProductInline(admin.TabularInline):
    model = ProductSet.products.through
    extra = 2


@admin.register(ProductSet)
class ProductSetAdmin(SortableAdminMixin, admin.ModelAdmin):
    inlines = [ProductSetProductInline]
    fields = ['name', 'sort', 'is_active']