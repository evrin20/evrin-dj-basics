from django.contrib import admin

# Register your models here,
from .models import Post , Author


class PostAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author','publish_date']
    list_filter  = ['author','tags','publish_date']
    search_fields = ['titlr','content'] 


admin.site.register(Post,PostAdmin)
admin.site.register(Author)