# Generated by Django 2.1.4 on 2019-01-22 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20190119_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='type',
            field=models.CharField(choices=[('Card', '单词页面'), ('Library', '绘本馆页面'), ('Video', '视频页面')], max_length=100, verbose_name='类型'),
        ),
    ]
