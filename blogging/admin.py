from django.contrib import admin
from blogging.models import Post, Category

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    exclude = ('posts',)

class CategoryInLine(admin.TabularInline):
    model = Category.posts.through

class PostAdmin(admin.ModelAdmin):
    inlines = [CategoryInLine, ]

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)

