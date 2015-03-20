from django.contrib import admin
from models import Post, Post_image

class PostImagesInline(admin.TabularInline):
	model = Post_image
	extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets =  (None,
        {'fields': ('title', 'date', 'preview', 'content', 'thumbnail',)}
    ),
    inlines = [PostImagesInline]
    list_display = ('title', 'preview_image', 'date',)


admin.site.register(Post, PostAdmin)