from django.contrib import admin
from models import Contact


class ContactAdmin(admin.ModelAdmin):
	list_display = ('author_name', 'datetime')

admin.site.register(Contact, ContactAdmin)