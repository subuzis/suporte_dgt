# Generated by Django 3.2 on 2022-01-21 14:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pendencias', '0028_alter_pendenciasuporte_observacao'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pendenciasuporte',
            name='image',
        ),
    ]