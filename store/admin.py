from django.contrib import admin
from jalali_date.admin import ModelAdmin, ModelAdminJalaliMixin, TabularInlineJalaliMixin
from .models import Product


# Register your models here.


class ProductInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = Product


# @admin.register(Product)
class ProductModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = ProductInline
    fields = ['created_at', 'updated_at']


admin.site.register(Product)
# admin.ACTION_CHECKBOX_NAME = ['cache']