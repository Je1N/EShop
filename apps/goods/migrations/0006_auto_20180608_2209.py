# Generated by Django 2.0.6 on 2018-06-08 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_auto_20180608_2038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodscategory',
            name='category_type',
            field=models.IntegerField(choices=[(1, '一级类目'), (2, '二级类目'), (3, '三级类目')], help_text='类别级别', max_length=30, verbose_name='类别级别'),
        ),
    ]
