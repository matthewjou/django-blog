from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Post(models.Model):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title
    

class Category(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True, related_name='categories')

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = 'Categories' 


# TODO: Create an InlineModelAdmin to represent Categories on the Post admin view.
class CategoryInline(admin.TabularInline):
    model = Category.posts.through


# TODO: Create a ModelAdmin class for the Post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    list_filter = ('published_date', 'author')
    search_fields = ('title', 'text')
    inlines = [CategoryInline]


# TODO: Create a ModelAdmin class for Category model
# exclude the ‘posts’ field from the form in your Category admin
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')
    exclude = ('posts',)

