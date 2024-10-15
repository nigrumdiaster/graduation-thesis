# Generated by Django 5.1 on 2024-10-15 22:01

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TinTuc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('TieuDe', models.CharField(max_length=500)),
                ('AnhChinh', models.ImageField(default='uploads/noimage.jpg', upload_to='uploads/')),
                ('The', models.CharField(max_length=255)),
                ('NoiDung', ckeditor.fields.RichTextField()),
                ('DuongDan', models.SlugField(blank=True, max_length=550, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Bài Viết',
                'verbose_name_plural': 'Bài Viết',
            },
        ),
    ]
