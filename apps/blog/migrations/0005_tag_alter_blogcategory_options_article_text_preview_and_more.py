# Generated by Django 4.1.4 on 2022-12-16 14:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name': 'Категория блога', 'verbose_name_plural': 'Категории блога'},
        ),
        migrations.AddField(
            model_name='article',
            name='text_preview',
            field=models.TextField(blank=True, null=True, verbose_name='Текст-превью'),
        ),
        migrations.AddField(
            model_name='blogcategory',
            name='img',
            field=models.ImageField(null=True, upload_to='blog/category/', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogcategory', verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='article',
            name='tags',
            field=models.ManyToManyField(blank=True, to='blog.tag', verbose_name='Теги'),
        ),
    ]
