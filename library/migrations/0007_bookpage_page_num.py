# Generated by Django 2.1.4 on 2019-03-15 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0006_auto_20190120_2341'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookpage',
            name='page_num',
            field=models.IntegerField(default=0, verbose_name='页码'),
        ),
    ]