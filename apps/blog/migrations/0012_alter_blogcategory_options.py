# Generated by Django 4.1.4 on 2023-01-07 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_delete_product_alter_article_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name': 'Категорії блогу', 'verbose_name_plural': 'Категорії блогу'},
        ),
    ]