from django.contrib import admin
from jalali_date.admin import TabularInlineJalaliMixin, ModelAdminJalaliMixin, ModelAdmin

# Register your models here.
from blog.models import Post


class PostInline(TabularInlineJalaliMixin, admin.TabularInline):
    model = Post


class PostModelAdmin(ModelAdminJalaliMixin, admin.ModelAdmin):
    inlines = PostInline
    fields = ['created_at', 'updated_at']


admin.site.register(Post)
