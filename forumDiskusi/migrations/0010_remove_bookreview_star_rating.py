# Generated by Django 4.2.6 on 2023-10-28 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forumDiskusi', '0009_bookreview_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreview',
            name='star_rating',
        ),
    ]
