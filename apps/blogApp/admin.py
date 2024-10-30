from django.contrib import admin
from .models import Author,Article,ArticleGallery,ArticleGroup

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=('name','family','slug','email','is_active')
    



@admin.register(ArticleGroup)
class ArticleGroupAdmin(admin.ModelAdmin):
    list_display=('group_title',)

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display=('title','register_date','slug','view_number')
    


@admin.register(ArticleGallery)
class ArticleGalleryAdmin(admin.ModelAdmin):
    list_display=('image_name','article')
    