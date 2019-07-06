# Generated by Django 2.1.4 on 2019-04-30 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0010_auto_20190427_1521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.CardType', verbose_name='卡片类型'),
        ),
        migrations.AlterField(
            model_name='cardtype',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.ProductType', verbose_name='产品'),
        ),
    ]
