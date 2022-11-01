# Generated by Django 4.1 on 2022-11-01 07:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Wilayah',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kota', models.CharField(max_length=20)),
                ('kebutuhan', models.TextField(default='')),
                ('address', models.TextField()),
                ('kuota_max', models.IntegerField()),
                ('kuota_terisi', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('jangka_waktu', models.DateField()),
                ('pj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
