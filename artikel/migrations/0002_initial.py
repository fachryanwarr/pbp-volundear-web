# Generated by Django 4.1 on 2022-11-01 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('artikel', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artikel',
            name='penulis',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
