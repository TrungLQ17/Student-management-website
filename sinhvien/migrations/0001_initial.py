# Generated by Django 5.0.6 on 2024-05-24 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeDaiHoc',
            fields=[
                ('ma_sv', models.IntegerField(primary_key=True, serialize=False)),
                ('ho_ten', models.CharField(max_length=100)),
                ('dia_chi', models.CharField(blank=True, max_length=100, null=True)),
                ('tong_tc', models.IntegerField(default=0)),
                ('diem_tb', models.FloatField(default=0)),
                ('ten_lv', models.CharField(blank=True, max_length=100)),
                ('diem_lv', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='VB2',
            fields=[
                ('ma_sv', models.IntegerField(primary_key=True, serialize=False)),
                ('ho_ten', models.CharField(max_length=100)),
                ('dia_chi', models.CharField(blank=True, max_length=100, null=True)),
                ('tong_tc', models.IntegerField(default=0)),
                ('diem_tb', models.FloatField(default=0)),
                ('diem_tot_nghiep', models.FloatField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TotNghiep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nam_totnghiep', models.IntegerField()),
                ('dot_totnghiep', models.IntegerField()),
                ('he_daihoc', models.ManyToManyField(blank=True, to='sinhvien.hedaihoc')),
                ('vb2', models.ManyToManyField(blank=True, to='sinhvien.vb2')),
            ],
        ),
    ]