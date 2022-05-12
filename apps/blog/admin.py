from django.contrib import admin
from apps.blog.models import Post, PostImage


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created', 'status')
    list_filter = ('status', 'created', 'created', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'created'
    ordering = ['status', 'created']


admin.site.register(Post, PostAdmin)


class PostImageAdmin(admin.ModelAdmin):
    list_display = ('post', 'image', 'created')
    list_filter = ('created', 'post')
    ordering = ['created']


admin.site.register(PostImage, PostImageAdmin)
