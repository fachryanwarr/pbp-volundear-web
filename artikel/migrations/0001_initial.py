# Generated by Django 4.1 on 2022-11-01 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artikel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('judul', models.CharField(max_length=100)),
                ('rilis', models.DateField(auto_now_add=True)),
                ('pembuka', models.TextField(default=None)),
                ('isi', models.TextField()),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
