# Generated by Django 4.2.6 on 2023-10-27 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forumDiskusi', '0002_alter_bookreview_book_alter_bookreview_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookreview',
            name='reviewer_name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
    ]