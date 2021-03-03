from re import S
from instagram.models import Post
from django.contrib import admin

# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['pk', 'message', 'message_length',
                    'is_public', 'created_at', 'updated_at', ]
    list_display_links = ['message']
    list_filter = ['is_public', 'created_at', ]
    search_fields = ['message']

    def message_length(self, instance):
        return f"{len(instance.message)} 글자"
    message_length.short_description = "메세지 글자수"
# admin.site.register(Post, PostAdmin)
