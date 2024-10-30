from django.db import models
from django.utils import timezone

class Visitor_Group(models.Model):
    Group_title=models.CharField(max_length=50,verbose_name="عنوان گروه")
    
    def __str__(self):
        return f'{self.Group_title}'
     
    class Meta:
        verbose_name="بازدید کننده"
        verbose_name_plural="بازدید کننده ها"
        db_table="t_Visitor_Group"
     
    
class Place(models.Model):
    place_title=models.CharField(max_length=50,verbose_name="عنوان مکان")
    Origina_photo=models.ImageField(upload_to="images/garden",verbose_name='عکس اصلی')
    Time_Visit=models.DateTimeField(default=timezone.now,verbose_name='ساعت بازدید')
    Description=models.TextField(verbose_name='اطلاعات بیشتر')
    Rules=models.CharField(max_length=200,verbose_name='قوانین')
    def __str__(self):
        return f'{self.place_title}'
     
    class Meta:
        verbose_name="مکان"
        verbose_name_plural="مکان ها"
        db_table="t_Place"
     
    
    
class Ticket_Price(models.Model):
     group_visit=models.ForeignKey(Visitor_Group,on_delete=models.CASCADE,verbose_name='گروه بازدید')
     place_visit=models.ForeignKey(Place,on_delete=models.CASCADE,verbose_name="مکان بازدید")
     Ticket_price=models.IntegerField(verbose_name=" بهای بلیط")
     
     def __str__(self):
         return f'{self.group_visit}\t{self.place_visit}\t{self.Ticket_price}'
     
     class Meta:
        verbose_name="قیمت بلیط"
        verbose_name_plural="قیمت بلیط ها"
        db_table="t_Ticket_Price"
     
class Message(models.Model):
    name=models.CharField(max_length=50,verbose_name="نام")
    family=models.CharField(max_length=50,verbose_name="نام خانوادگی")
    email=models.EmailField(max_length=254,verbose_name="ایمیل")
    title_message=models.CharField(max_length=60,verbose_name="موضوع پیام")
    text_message=models.TextField(verbose_name="متن پیام")
    Time_message=models.DateTimeField(default=timezone.now,verbose_name='تاریخ ثبت پیام')
    show_message=models.BooleanField(verbose_name="دیده شده/دیده نشده",default=False)
    def __str__(self):
        return f'{self.name}\t{self.family}\t{self.email}\t{self.title_message}\t{self.Time_message}\t{self.show_message}'
     
    class Meta:
        verbose_name="پیام"
        verbose_name_plural="پیام ها"
        db_table="t_Message"
    
    