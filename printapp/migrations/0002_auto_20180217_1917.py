# Generated by Django 2.0.2 on 2018-02-17 12:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historybayar',
            name='bayar_now',
            field=models.DecimalField(decimal_places=2, max_digits=14, verbose_name='pembayaran sekarang'),
        ),
        migrations.AlterField(
            model_name='kontrak',
            name='nhari_har',
            field=models.IntegerField(default=0, verbose_name='masa pemeliharaan (hari)'),
        ),
        migrations.AlterField(
            model_name='kontrak',
            name='tgl_due',
            field=models.DateField(default=datetime.date.today, verbose_name='tgl jatuh tempo'),
        ),
        migrations.AlterField(
            model_name='termin',
            name='nth_termin',
            field=models.IntegerField(default=1, verbose_name='termin ke-'),
        ),
    ]
