# Generated by Django 2.1.4 on 2019-04-30 02:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0007_bookpage_page_num'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookpage',
            name='title',
        ),
        migrations.AlterField(
            model_name='bookpage',
            name='book',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Book', verbose_name='所属子绘本'),
        ),
        migrations.AlterField(
            model_name='bookpage',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Volume', verbose_name='所属绘本'),
        ),
        migrations.AlterField(
            model_name='volume',
            name='book_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.BookType', verbose_name='绘本类别'),
        ),
    ]
