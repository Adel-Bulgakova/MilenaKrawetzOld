from django.contrib import admin
from models import Portfolio, Portfolio_image

class PortfolioImagesInline(admin.TabularInline):
	model = Portfolio_image
	extra = 0

class PortfolioAdmin(admin.ModelAdmin):
    fieldsets =  (None,
        {'fields': ('title', 'about',)}
    ),
    inlines = [PortfolioImagesInline]
    list_display = ('title',)

admin.site.register(Portfolio, PortfolioAdmin)