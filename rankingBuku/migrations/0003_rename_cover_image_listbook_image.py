# Generated by Django 4.2.6 on 2023-10-29 12:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rankingBuku', '0002_listbook_cover_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listbook',
            old_name='cover_image',
            new_name='image',
        ),
    ]
