# Generated by Django 4.1 on 2022-10-11 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0009_dosenfkip_nomor_stafffkip_nomor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProdiFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor', models.CharField(max_length=300, null=True)),
                ('tahun', models.CharField(max_length=50)),
                ('kajur', models.CharField(max_length=100)),
            ],
        ),
    ]
