# Generated by Django 4.0.4 on 2022-04-19 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HBMS_App', '0004_checkin_checkout'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkin_checkout',
            name='room_id',
            field=models.CharField(default='', max_length=20),
        ),
    ]