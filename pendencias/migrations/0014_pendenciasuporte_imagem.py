# Generated by Django 3.2 on 2022-01-10 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pendencias', '0013_alter_pendenciasuporte_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendenciasuporte',
            name='imagem',
            field=models.FileField(blank=True, upload_to='PendenciaSuporte_image'),
        ),
    ]