from django.contrib import admin
from blog.models import Article, Comments


class ArticleInline(admin.StackedInline):
    model=Comments
    extra = 2
class ArticleAdmin(admin.ModelAdmin):
    fields = ['title','text', 'date']
    inlines = [ArticleInline]


admin.site.register(Article, ArticleAdmin)


