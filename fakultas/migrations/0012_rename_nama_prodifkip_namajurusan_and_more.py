# Generated by Django 4.1 on 2022-10-11 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakultas', '0011_prodifkip_nama_alter_prodifkip_kajur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='prodifkip',
            old_name='nama',
            new_name='namajurusan',
        ),
        migrations.RenameField(
            model_name='prodifkip',
            old_name='kajur',
            new_name='namakajur',
        ),
    ]
