# Generated by Django 3.2.12 on 2022-04-09 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0041_auto_20220409_1629'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='Цена')),
                ('number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.number', verbose_name='Номер')),
            ],
            options={
                'verbose_name': 'Цены',
                'verbose_name_plural': 'Цены на номера',
            },
        ),
        migrations.CreateModel(
            name='PricePeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateField(verbose_name='Начало периода')),
                ('end', models.DateField(verbose_name='Конец периода')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.hotel', verbose_name='Гостиница')),
            ],
        ),
        migrations.DeleteModel(
            name='NumberPrice',
        ),
        migrations.AddField(
            model_name='price',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hotel.priceperiod', verbose_name='Период'),
        ),
    ]
