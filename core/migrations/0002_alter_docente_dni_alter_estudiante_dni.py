# Generated by Django 4.2.7 on 2023-11-14 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docente',
            name='dni',
            field=models.IntegerField(unique=True, verbose_name='DNI'),
        ),
        migrations.AlterField(
            model_name='estudiante',
            name='dni',
            field=models.IntegerField(unique=True, verbose_name='DNI'),
        ),
    ]