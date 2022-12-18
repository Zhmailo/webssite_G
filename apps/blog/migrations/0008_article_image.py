# Generated by Django 4.1.4 on 2022-12-16 15:56

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogcategory_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/article/', verbose_name='Изображение'),
        ),
    ]
