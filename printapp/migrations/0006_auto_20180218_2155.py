# Generated by Django 2.0.2 on 2018-02-18 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('printapp', '0005_auto_20180218_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ppm',
            name='anggota',
            field=models.CharField(choices=[('SPS POH', 'Supervisor Senior Perencanaan Operasi Pemeliharaan'), ('SPS HPL', 'Supervisor Senior Pemeliharaan Sipil'), ('SPS GHW', 'Supervisor Senior Geologi dan Hidrologi Waduk'), ('SPS LLK', 'Supervisor Senior Lahan dan Lingkungan'), ('SPS KKK', 'Supervisor Senior Kesehatan dan Keselamatan Kerja'), ('SPS CBM', 'Supervisor Senior Condition Based Monitoring'), ('SPS OTG', 'Supervisor Senior Outage'), ('SPS REO', 'Supervisor Senior Reliability'), ('SPS PUK', 'Supervisor Senior Perencanaan Unit dan Kinerja'), ('SPS MUM', 'Supervisor Senior Umum'), ('SPS KAS', 'Supervisor Senior Keamanan dan Humas'), ('SPS SIS', 'Supervisor Senior Sistem Informasi'), ('SPS HAR', 'Supervisor Senior Pemeliharaan'), ('SPS OPN', 'Supervisor Senior Operasi'), ('AMU RENOP', 'AMU Perencanaan Operasi')], default='SPS HAR', max_length=9),
        ),
        migrations.AlterField(
            model_name='ppm',
            name='sekretaris',
            field=models.CharField(choices=[('SPS POH', 'Supervisor Senior Perencanaan Operasi Pemeliharaan'), ('SPS HPL', 'Supervisor Senior Pemeliharaan Sipil'), ('SPS GHW', 'Supervisor Senior Geologi dan Hidrologi Waduk'), ('SPS LLK', 'Supervisor Senior Lahan dan Lingkungan'), ('SPS KKK', 'Supervisor Senior Kesehatan dan Keselamatan Kerja'), ('SPS CBM', 'Supervisor Senior Condition Based Monitoring'), ('SPS OTG', 'Supervisor Senior Outage'), ('SPS REO', 'Supervisor Senior Reliability'), ('SPS PUK', 'Supervisor Senior Perencanaan Unit dan Kinerja'), ('SPS MUM', 'Supervisor Senior Umum'), ('SPS KAS', 'Supervisor Senior Keamanan dan Humas'), ('SPS SIS', 'Supervisor Senior Sistem Informasi'), ('SPS HAR', 'Supervisor Senior Pemeliharaan'), ('SPS OPN', 'Supervisor Senior Operasi'), ('AMU RENOP', 'AMU Perencanaan Operasi')], default='SPS POH', max_length=9),
        ),
    ]
