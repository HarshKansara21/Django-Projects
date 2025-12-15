from django.contrib import admin
from .models import Contact, BlogPost, Newsletter

# Register your models here.

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['full_name', 'email', 'service', 'created_at']
    list_filter = ['service', 'created_at']
    search_fields = ['full_name', 'email', 'company']
    readonly_fields = ['created_at']

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'category', 'published', 'created_at']
    list_filter = ['published', 'category', 'created_at']
    search_fields = ['title', 'content', 'excerpt']
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ['created_at', 'updated_at']

@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['email', 'active', 'subscribed_at']
    list_filter = ['active', 'subscribed_at']
    search_fields = ['email']
    readonly_fields = ['subscribed_at']
