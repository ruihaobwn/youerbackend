# Generated by Django 2.1.4 on 2019-01-19 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poster',
            name='type',
            field=models.CharField(choices=[('Card', '单词页面'), ('Library', '绘本馆页面')], max_length=100, verbose_name='类型'),
        ),
    ]
