from django.contrib import admin
from .models import Post, PostImages, Likes, Comments


class PostImagesInline(admin.TabularInline):
    model = PostImages
    extra = 0

class PostAdmin(admin.ModelAdmin):
    inlines = [PostImagesInline]
    readonly_fields = ('date',)

admin.site.register(Post, PostAdmin)
admin.site.register(Likes)
admin.site.register(Comments)