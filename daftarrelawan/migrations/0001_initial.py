# Generated by Django 4.1 on 2022-11-02 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DaftarRelawan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('keahlian', models.CharField(max_length=50)),
                ('tanggal', models.DateTimeField()),
                ('jam', models.TimeField()),
            ],
        ),
    ]
