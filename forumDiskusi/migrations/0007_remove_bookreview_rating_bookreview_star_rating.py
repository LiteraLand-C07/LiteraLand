# Generated by Django 4.2.6 on 2023-10-27 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumDiskusi', '0006_remove_bookreview_star_rating_bookreview_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookreview',
            name='rating',
        ),
        migrations.AddField(
            model_name='bookreview',
            name='star_rating',
            field=models.PositiveSmallIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=1),
            preserve_default=False,
        ),
    ]