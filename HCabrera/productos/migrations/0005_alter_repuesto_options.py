# Generated by Django 3.2.3 on 2021-07-05 01:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0004_repuesto_descripcionrepuesto'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='repuesto',
            options={'permissions': (('administrador', 'Es administrador'), ('cliente', 'Es cliente'))},
        ),
    ]
