# Generated by Django 5.0.6 on 2024-08-22 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('introduction', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'پیام', 'verbose_name_plural': 'پیام ها'},
        ),
        migrations.AlterModelOptions(
            name='place',
            options={'verbose_name': 'مکان', 'verbose_name_plural': 'مکان ها'},
        ),
        migrations.AlterModelOptions(
            name='ticket_price',
            options={'verbose_name': 'قیمت بلیط', 'verbose_name_plural': 'قیمت بلیط ها'},
        ),
        migrations.AlterModelTable(
            name='message',
            table='t_Message',
        ),
        migrations.AlterModelTable(
            name='place',
            table='t_Place',
        ),
        migrations.AlterModelTable(
            name='ticket_price',
            table='t_Ticket_Price',
        ),
    ]