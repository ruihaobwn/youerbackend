# Generated by Django 2.1.4 on 2019-01-23 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0005_video_video_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='video_url',
            field=models.FileField(blank=True, max_length=80, null=True, upload_to='', verbose_name='视频源'),
        ),
    ]