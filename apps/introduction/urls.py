from django.urls import path
from .views import (create_message,show_message,delete_message,Update_message,
show_list_Place,show_garden_history,show_garden_part,download_path_garden,show_part_detail)

app_name="introduction"
urlpatterns = [
    path("create_message/",create_message.as_view(),name="create_message"),
    path('show_list_massege/',show_message.as_view(),name="show_list_massege"),
    path('delete_message/<int:pk>/',delete_message.as_view(),name="delete_message"),
    path('Update_message/<int:pk>/',Update_message.as_view(),name="Update_message"),
    path('garden_history/',show_garden_history,name="garden_history"),
    path('show_list_Place/',show_list_Place,name="show_Place"),
    path('show_garden_part/',show_garden_part,name="show_garden_part"),
    path('show_garden_part/<int:id>/',show_part_detail,name="show_part_detail"),
    path('download_path_garden/',download_path_garden,name="download_path_garden")
]
