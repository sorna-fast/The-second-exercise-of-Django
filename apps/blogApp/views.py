from django.shortcuts import render
from .models import Article,Author
from django.conf import settings
import os
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
# Create your views here.


def show_articles(request):
    articles = Article.objects.all()
    articles_authors= Article.author.through.objects.all()
    authors = Author.objects.all()
    context={
        'articles':articles,
        "articles_authors":articles_authors,
        'authors':authors,
        'media_url':settings.MEDIA_URL
        }
    return render(request,'articles_app/blog.html',context)

#______________________________________________________________________________________________

def show_blog_detils(request,slug):
    article=Article.objects.get(slug = slug)
    image_List= os.listdir(settings.MEDIA_ROOT+"/images/blog/articles_"+str(article.id))
    article.view_number+=1
    article.save()
    articles_authors = Article.objects.get(id=article.id).author.through.objects.all()
    authors = Author.objects.all()
    context={
        'article':article,
        'articles_authors':articles_authors,
        'authors':authors,
        'media_url':settings.MEDIA_URL,
        'image_List':image_List,
        'article.view_number':article.view_number
        }
    return render(request,'articles_app/blog_details.html',context)

#______________________________________________________________________________________________

def show_article_pdf(request,article_id):
    fs = FileSystemStorage()
    filename=str(article_id)+".pdf"
    file_path="pdf/blog/articlepdf/"+filename
    if fs.exists(file_path):
        with fs.open(file_path) as pdf:
            respons = HttpResponse(pdf,content_type="application/pdf")
            respons['Content-Disposition'] = 'inline;filename='+"article_"+filename
            return respons
    else:
        return HttpResponse("The requested pdf file ws not found in our server")