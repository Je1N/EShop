# Generated by Django 2.0.6 on 2018-06-07 20:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_aperation', '0003_auto_20180607_2003'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'verbose_name': '收货地址', 'verbose_name_plural': '收货地址'},
        ),
        migrations.AlterModelOptions(
            name='userleavingmessage',
            options={'verbose_name': '用户留言', 'verbose_name_plural': '用户留言'},
        ),
    ]
