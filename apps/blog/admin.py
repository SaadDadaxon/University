from django.contrib import admin
from .models import Post, Body, Comment


class BodyInline(admin.TabularInline):
    model = Body
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = (BodyInline, )
    list_display = ('id', 'title', 'author', "created_date")
    search_fields = ('title', )
    list_filter = ('category', 'tags')
    filter_horizontal = ('tags',)
    date_hierarchy = 'created_date'


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'parent_comment', 'top_level_comment_id', 'created_date')
    search_fields = ('author__first_name', 'author__last_name', 'author__username', 'post')
    date_hierarchy = 'created_date'
