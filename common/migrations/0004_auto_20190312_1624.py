# Generated by Django 2.1.4 on 2019-03-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20190123_0110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='link_url',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='跳转地址'),
        ),
    ]
