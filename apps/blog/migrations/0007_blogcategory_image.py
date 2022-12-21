# Generated by Django 4.1.4 on 2022-12-16 15:46

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blogcategory_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogcategory',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
    ]
