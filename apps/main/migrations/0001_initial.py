# Generated by Django 4.1.4 on 2023-02-27 04:57

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title')),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords')),
                ('name', models.CharField(max_length=128, verbose_name='Назван')),
                ('slug', models.SlugField(unique=True)),
                ('text', tinymce.models.HTMLField(null=True, verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Інформаційна сторінка',
                'verbose_name_plural': 'Інформаційні сторінки',
            },
        ),
    ]
