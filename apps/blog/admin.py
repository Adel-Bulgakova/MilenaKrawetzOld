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


from django.contrib.admin.widgets import AdminFileWidget
from django.utils.translation import ugettext as _
from django.utils.safestring import mark_safe

class AdminImageWidget(AdminFileWidget):
    def render(self, name, value, attrs=None):
        output = []
        if value and getattr(value, "url", None):
            image_url = value.url
            file_name=str(value)
            output.append(u' <a href="%s" target="_blank"><img src="%s" alt="%s" /></a> %s ' % \
                (image_url, image_url, file_name, _('Change:')))
        output.append(super(AdminFileWidget, self).render(name, value, attrs))
        return mark_safe(u''.join(output))



admin.site.register(Post, PostAdmin)