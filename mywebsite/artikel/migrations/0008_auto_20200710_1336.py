# Generated by Django 2.2 on 2020-07-10 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('artikel', '0007_auto_20200710_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelartikel',
            name='image',
            field=models.ImageField(upload_to='upload/'),
        ),
    ]
