from django.contrib import admin

# Register your models here.
from .models import SocialUser, Post, Friend, Comment, Interests

class SocialUserModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'email', 'created_date']
    list_display_links = ['created_date']
    list_filter = ['name', 'surname']
    search_fields = ['name', "surname", 'email', 'city']

    class Meta:
        model = SocialUser


class PostModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_date']
    list_display_links = ['created_date']
    list_filter = ['created_date']
    search_fields = ['title', "text"]

    class Meta:
        model = Post


class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'created')


admin.site.register(Post, PostModelAdmin)
admin.site.register(SocialUser, SocialUserModelAdmin)
admin.site.register(Friend)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Interests)
