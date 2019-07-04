from django.contrib import admin
from jalali_date.admin import TabularInlineJalaliMixin, ModelAdminJalaliMixin, ModelAdmin

# Register your models here.
from pages.models import Contact


class ContactInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = Contact


class ContactModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = ContactInline
    fields = ['created_at', 'updated_at']


admin.site.register(Contact)
