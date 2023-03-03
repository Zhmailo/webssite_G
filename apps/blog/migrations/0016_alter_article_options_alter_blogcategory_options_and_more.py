# Generated by Django 4.1.4 on 2023-02-28 16:16

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_alter_article_options_alter_blogcategory_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name': 'Стаття', 'verbose_name_plural': 'Статті'},
        ),
        migrations.AlterModelOptions(
            name='blogcategory',
            options={'verbose_name': 'Категорія блога', 'verbose_name_plural': 'Категорії блога'},
        ),
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Тег', 'verbose_name_plural': 'Теги'},
        ),
        migrations.RenameField(
            model_name='article',
            old_name='tags',
            new_name='tag',
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_description',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Description'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_keywords',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Keywords'),
        ),
        migrations.AddField(
            model_name='tag',
            name='meta_title',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Meta Title'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blogcategory', verbose_name='Категорія'),
        ),
        migrations.AlterField(
            model_name='article',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/category/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(verbose_name='Дата публікації'),
        ),
        migrations.AlterField(
            model_name='article',
            name='text_preview',
            field=models.TextField(blank=True, null=True, verbose_name="Текст-прев'ю"),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='image',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/category/', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='blogcategory',
            name='name',
            field=models.CharField(max_length=255, verbose_name="Ім'я категорії"),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Напишіть тег'),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name="Ваше ім'я")),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('text', models.TextField(verbose_name='Текст')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активовано')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата створення')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.article', verbose_name='Стаття')),
            ],
            options={
                'verbose_name': 'Коментарій',
                'verbose_name_plural': 'Коментарі',
            },
        ),
    ]
