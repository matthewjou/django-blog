from django.contrib import admin
from blogging.models import Post, Category, PostAdmin, CategoryAdmin

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
