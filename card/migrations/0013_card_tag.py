# Generated by Django 2.2.1 on 2019-06-09 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0012_auto_20190430_0336'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='tag',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='标识'),
        ),
    ]