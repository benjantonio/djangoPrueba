# Generated by Django 3.2.3 on 2021-06-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0003_alter_servicio_descripcionservicio'),
    ]

    operations = [
        migrations.AddField(
            model_name='repuesto',
            name='descripcionRepuesto',
            field=models.CharField(default=1, max_length=300, verbose_name='Descripción repuesto'),
            preserve_default=False,
        ),
    ]
