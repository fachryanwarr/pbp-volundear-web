# Generated by Django 4.1 on 2022-11-02 12:12

from django.db import migrations, models
import django.db.models.deletion


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
        migrations.CreateModel(
            name='Komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('waktu', models.DateField(auto_now_add=True)),
                ('deskripsi', models.TextField()),
                ('artikel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='artikel.artikel')),
            ],
            options={
                'ordering': ['-pk'],
            },
        ),
    ]
