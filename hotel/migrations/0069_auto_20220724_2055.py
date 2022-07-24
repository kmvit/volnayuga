# Generated by Django 3.2.12 on 2022-07-24 17:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0068_alter_price_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='priceperiod',
            options={'verbose_name': '', 'verbose_name_plural': 'Периоды цен на гостиницы'},
        ),
        migrations.AddField(
            model_name='priceperiod',
            name='extra_bed',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена за дополнительное место'),
        ),
        migrations.AddField(
            model_name='priceperiod',
            name='number',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotel.number', verbose_name='Номер'),
        ),
        migrations.AddField(
            model_name='priceperiod',
            name='price',
            field=models.IntegerField(blank=True, null=True, verbose_name='Цена'),
        ),
        migrations.DeleteModel(
            name='Price',
        ),
    ]
