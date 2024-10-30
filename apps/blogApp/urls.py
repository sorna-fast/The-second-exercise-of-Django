from django.urls import path, re_path
from .views import *

app_name = "blog"

urlpatterns = [
    path("",show_articles,name="blog_show"),
    path("<str:slug>/",show_blog_detils,name="blog_details"),
    path('articlepdf/<int:article_id>/',show_article_pdf,name="article_pdf")
    
]