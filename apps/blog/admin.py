from django.contrib import admin
from models import Post, Post_image

# class ImagesInline(admin.TabularInline):
#     model = Post_images
#
# class PostAdmin(admin.ModelAdmin):
#     inlines = [
#         ImagesInline,
#     ]

admin.site.register(Post)
admin.site.register(Post_image)