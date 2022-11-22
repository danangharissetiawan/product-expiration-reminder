from django.contrib import admin
from . import models


# admin.site.register(models.BaseProduct, BaseProductAdmin)
@admin.register(models.ProductPackaging)
class ProductPackagingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'label', 'expiry_date', 'date_added')
    list_filter = ('category', 'label', 'expiry_date')
    search_fields = ('name', 'category', 'label', 'expiry_date', 'date_added')
    ordering = ('-date_added',)
    prepopulated_fields = {'slug': ('name', 'expiry_date')}


@admin.register(models.ProductNonPackaging)
class ProductNonPackagingAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'quality', 'label', 'expiry_date', 'date_added')
    list_filter = ('category', 'quality', 'label', 'expiry_date')
    search_fields = ('name', 'category', 'quality', 'label', 'expiry_date', 'date_added')
    ordering = ('-date_added',)
    prepopulated_fields = {'slug': ('name', 'expiry_date')}


@admin.register(models.Barcode)
class BarcodeAdmin(admin.ModelAdmin):

    list_display = ('name', 'barcode')
    search_fields = ('name', 'barcode')
    ordering = ('name',)


