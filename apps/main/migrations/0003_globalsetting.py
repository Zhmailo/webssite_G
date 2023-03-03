# Generated by Django 4.1.4 on 2023-03-02 11:20

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_page_name_alter_page_text_productset'),
    ]

    operations = [
        migrations.CreateModel(
            name='GlobalSetting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meta_title', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title')),
                ('meta_description', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description')),
                ('meta_keywords', models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords')),
                ('main_text', tinymce.models.HTMLField(verbose_name='Текст на главной')),
                ('footer_text', models.CharField(max_length=255, verbose_name='Текст в футере')),
                ('logo', models.ImageField(null=True, upload_to='main', verbose_name='Изображение')),
            ],
            options={
                'verbose_name': 'Настройки',
                'verbose_name_plural': 'Настройки',
            },
        ),
    ]
