# Generated by Django 3.2.12 on 2022-04-02 10:50

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0005_auto_20220331_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='region',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, null=True, verbose_name='Описание'),
        ),
    ]
