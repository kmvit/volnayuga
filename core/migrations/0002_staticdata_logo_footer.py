# Generated by Django 3.2.12 on 2022-04-13 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staticdata',
            name='logo_footer',
            field=models.ImageField(blank=True, upload_to='core/images', verbose_name='Логотип в подвале'),
        ),
    ]
