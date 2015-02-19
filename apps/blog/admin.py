from django.contrib import admin
from models import Post, Post_image

class PostImagesInline(admin.TabularInline):
	model = Post_image
	extra = 0


class PostAdmin(admin.ModelAdmin):
    fieldsets =  (None,
        {'fields': ('title', 'date', 'published', 'preview', 'content',)}
    ),
    inlines = [PostImagesInline]
    list_display = ('title', 'date', 'published',)


admin.site.register(Post, PostAdmin)
# admin.site.register(Post)
# admin.site.register(Post_image)