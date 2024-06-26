# Generated by Django 2.1.4 on 2019-01-08 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('name', models.CharField(max_length=80, unique=True, verbose_name='图片名称')),
                ('picture', models.FileField(max_length=80, upload_to='', verbose_name='卡片图片')),
            ],
            options={
                'verbose_name': '卡片',
                'verbose_name_plural': '卡片',
            },
        ),
        migrations.CreateModel(
            name='CardAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('type', models.CharField(choices=[('Word', '单词'), ('Sentence', '句子')], max_length=25, verbose_name='音频类型')),
                ('url', models.FileField(max_length=80, upload_to='audio/card', verbose_name='资源地址')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.Card')),
            ],
            options={
                'verbose_name': '单词卡片资源',
                'verbose_name_plural': '单词卡片资源',
            },
        ),
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('title', models.CharField(max_length=80, verbose_name='卡片类别名称')),
                ('image_file', models.FileField(upload_to='', verbose_name='图片')),
            ],
            options={
                'verbose_name': '卡片类别',
                'verbose_name_plural': '卡片类别',
            },
        ),
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='备注')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(db_index=True, default=False)),
                ('sup_type', models.CharField(choices=[('English', '英文教具'), ('Chinese', '中文教具')], max_length=80, verbose_name='语言类型')),
                ('sub_type', models.CharField(max_length=80, verbose_name='产品类别')),
                ('image', models.FileField(upload_to='', verbose_name='图片')),
            ],
            options={
                'verbose_name': '卡片产品类型',
                'verbose_name_plural': '卡片产品类型',
            },
        ),
        migrations.AddField(
            model_name='cardtype',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.ProductType'),
        ),
        migrations.AddField(
            model_name='card',
            name='card_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.CardType'),
        ),
    ]
