# Generated by Django 3.2.12 on 2022-06-08 21:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('seo', '0002_seofortype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='seofortype',
            options={'verbose_name': 'SEO для страницы типа жилья', 'verbose_name_plural': 'SEO для страниц типов жилья'},
        ),
        migrations.RemoveField(
            model_name='seofortype',
            name='title',
        ),
    ]
