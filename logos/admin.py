from django.contrib import admin
from logos.models import Post


class PostAdmin(admin.ModelAdmin):
	date_hierarchy = 'pub_date'
	list_display = ('title', 'pub_date')
	prepopulated_fields = {'slug': ('title',)}
	search_fields = ('title', 'slug', 'body')

admin.site.register(Post, PostAdmin)
