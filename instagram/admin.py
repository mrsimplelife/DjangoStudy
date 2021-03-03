from django.utils.safestring import mark_safe
from django.contrib import admin
from instagram.models import Comment, Post
# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'photo_tag', 'message', 'message_length',
                    'is_public', 'created_at', 'updated_at', ]
    list_display_links = ['message']
    list_filter = ['is_public', 'created_at', ]
    search_fields = ['message']

    def photo_tag(self, instance: Post):
        if instance.photo:
            return mark_safe(f'<img src="{instance.photo.url}" style="width:20px;heigth:20px;"/>')

    def message_length(self, instance):
        return f"{len(instance.message)} 글자"
    message_length.short_description = '메세지 글자수'
# admin.site.register(Post, PostAdmin)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
