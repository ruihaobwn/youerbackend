# Generated by Django 2.1.4 on 2019-01-09 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0002_auto_20190109_2318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='video',
            field=models.FileField(blank=True, max_length=80, null=True, upload_to='video/card', verbose_name='卡片视频'),
        ),
    ]
