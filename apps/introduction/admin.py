from django.contrib import admin
from .models import Ticket_Price,Place,Visitor_Group,Message

@admin.register(Ticket_Price)
class Ticket_Price_admin(admin.ModelAdmin):
    list_display=["group_visit","place_visit","Ticket_price"]



@admin.register(Place)
class Place_admin(admin.ModelAdmin):
    list_display=["place_title","Origina_photo","Time_Visit","Description","Rules"]
    
    
@admin.register(Visitor_Group)
class Place_admin(admin.ModelAdmin):
    list_display=["Group_title"]
    
@admin.register(Message)
class Place_admin(admin.ModelAdmin):
    list_display=["name","family","email","title_message","text_message","Time_message","show_message"]