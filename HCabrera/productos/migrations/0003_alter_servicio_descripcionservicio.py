# Generated by Django 3.2.3 on 2021-06-11 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_servicio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='descripcionServicio',
            field=models.CharField(max_length=120, verbose_name='Descripcion servicio'),
        ),
    ]
