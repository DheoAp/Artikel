# Generated by Django 2.2 on 2020-07-07 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ModelArtikel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gambar', models.ImageField(upload_to='upload/')),
                ('judul', models.CharField(max_length=50)),
                ('kategori', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('penulis', models.CharField(max_length=50)),
                ('publish', models.TimeField(auto_now_add=True)),
                ('update', models.TimeField(auto_now=True)),
                ('slug', models.SlugField(blank=True, editable=False)),
            ],
        ),
    ]