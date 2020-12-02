from django.contrib import admin
from blog.models import Post, BlogComment ,Blog

admin.site.register((BlogComment))
@admin.register(Post)

class BlogAdmin(admin.ModelAdmin):
    list_display = ( 'field',)
    list_display_links =( 'field',)
    list_filter = ('field',)
    search_fields = ('field',)
    list_per_page = 25

admin.site.register(Blog, BlogAdmin) 

class PostAdmin(admin.ModelAdmin):
    class Media:
        js= ('tinyInject.js',)