# Generated by Django 3.2 on 2022-01-11 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendencias', '0026_auto_20220111_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pendenciasuporte',
            name='image',
            field=models.ImageField(blank=True, upload_to='pend_imgs'),
        ),
    ]
