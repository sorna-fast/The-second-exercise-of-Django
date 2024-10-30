from django.shortcuts import render
from django.views.generic.edit import CreateView,DeleteView,UpdateView
from django.views.generic import ListView
from .models import Message,Ticket_Price,Visitor_Group,Place
from django.urls import reverse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse,HttpResponseNotFound

class create_message(CreateView):
    model=Message
    fields=["name","family","email","title_message","text_message"]
    template_name="introduction/create_message.html"
    context_object_name="form"
    def get_success_url(self):
        return reverse("show_list_massege")

class show_message(ListView):
    model=Message
    template_name="introduction/list_massege.html"
    context_object_name="lists"
    
    
class delete_message(DeleteView):
    model=Message
    template_name="introduction/delete_message.html"
    fields="__all__"
    context_object_name="object"
    def get_success_url(self):
        return reverse("show_list_massege")
    
class Update_message(UpdateView):
    model=Message
    template_name="introduction/Update_message.html"
    fields=["name","family","text_message"]
    context_object_name="form"
    def get_success_url(self):
        return reverse("show_list_massege")
    
#=================================================================================
#  تاریجچه باغ 

def show_garden_history(request):
    return render(request,"introduction/show_garden_history.html")
 
#=============================================================
#برنامه و قوانین باغ


    
def show_list_Place(request):
    place=Place.objects.all()
    ticket_price=Ticket_Price.objects.all()
    
    context={
        "Places":place,
        "Ticket_Prices":ticket_price

    }

    return render(request,"introduction/show_list_Place.html",context)
#=====================================================================
#بخش های باغ 

def show_garden_part(request):
    place=Place.objects.all()
    context={
        "Places":place
    }

    return render(request,"introduction/show_garden_part.html",context)
#=====================================================================
#جزییات بخش ها

def show_part_detail(request,id):
    place=Place.objects.get(id=id)
    return render(request,"introduction/part_detail.html",{"place":place})
#=====================================================================
# مسیر بازدید

def download_path_garden(request):
    fs=FileSystemStorage()
    fie_name="pdf/ferdowsGardenPath.pdf"
    if fs.exists(fie_name):
        with fs.open(fie_name) as pdf:
            response=HttpResponse(pdf,content_type='application/pdf')
            response["Content-Disposition"]="attachment; filename=ferdowsGardenPath.pdf"
            return response
    else:
        return HttpResponseNotFound("File not found.....")
            



