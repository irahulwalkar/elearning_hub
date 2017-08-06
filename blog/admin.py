from django.contrib import admin
from .models import Post, Topic

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'topic')


admin.site.register(Topic)
admin.site.register(Post, PostAdmin)