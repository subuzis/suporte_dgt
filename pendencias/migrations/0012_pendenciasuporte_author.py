# Generated by Django 3.2 on 2022-01-07 15:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pendencias', '0011_alter_pendenciasuporte_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='pendenciasuporte',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
