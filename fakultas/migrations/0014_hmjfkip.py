# Generated by Django 4.1 on 2022-10-11 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0013_rename_tahun_prodifkip_tahunberdiri'),
    ]

    operations = [
        migrations.CreateModel(
            name='HmjFkip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomor', models.CharField(max_length=300, null=True)),
                ('namahmj', models.CharField(max_length=50)),
            ],
        ),
    ]