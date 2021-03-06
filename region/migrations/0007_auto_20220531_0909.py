# Generated by Django 3.2.12 on 2022-05-31 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0006_alter_region_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='region',
            name='h1_title',
            field=models.CharField(blank=True, max_length=100, verbose_name='Заголовок H1'),
        ),
        migrations.AddField(
            model_name='region',
            name='short_description',
            field=models.TextField(blank=True, verbose_name='Короткое описание в шапке'),
        ),
    ]
