# Generated by Django 2.1.4 on 2019-01-19 15:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='绘本名称')),
                ('picture', models.FileField(max_length=80, upload_to='', verbose_name='绘本图片')),
            ],
            options={
                'verbose_name': '绘本',
                'verbose_name_plural': '绘本',
            },
        ),
        migrations.CreateModel(
            name='BookPage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('title', models.CharField(max_length=80, unique=True, verbose_name='主题')),
                ('picture', models.FileField(max_length=80, upload_to='', verbose_name='图片')),
                ('audio_url', models.FileField(blank=True, max_length=80, null=True, upload_to='', verbose_name='音频')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.Book')),
            ],
            options={
                'verbose_name': '绘本页',
                'verbose_name_plural': '绘本页',
            },
        ),
        migrations.CreateModel(
            name='BookType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('title', models.CharField(max_length=80, verbose_name='类别名称')),
                ('image_file', models.FileField(upload_to='', verbose_name='图片')),
            ],
            options={
                'verbose_name': '绘本类别',
                'verbose_name_plural': '绘本类别',
            },
        ),
        migrations.CreateModel(
            name='Volume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='书册名称')),
                ('picture', models.FileField(max_length=80, upload_to='', verbose_name='书册图片')),
                ('book_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.BookType')),
            ],
            options={
                'verbose_name': '书册',
                'verbose_name_plural': '书册',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='book_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.BookType'),
        ),
        migrations.AddField(
            model_name='book',
            name='volume',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.Volume'),
        ),
    ]
