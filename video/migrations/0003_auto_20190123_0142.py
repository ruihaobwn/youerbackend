# Generated by Django 2.1.4 on 2019-01-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0002_auto_20190123_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='image_file',
            field=models.FileField(max_length=80, upload_to='', verbose_name='图片'),
        ),
    ]