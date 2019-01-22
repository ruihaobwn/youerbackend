# Generated by Django 2.1.4 on 2019-01-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20190120_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='book_type',
        ),
        migrations.AddField(
            model_name='book',
            name='description',
            field=models.TextField(default='', verbose_name='子绘本描述'),
            preserve_default=False,
        ),
    ]