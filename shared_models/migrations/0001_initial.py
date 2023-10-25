# Generated by Django 4.2.6 on 2023-10-15 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('author', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('publisher', models.CharField(max_length=255)),
                ('page_count', models.IntegerField()),
                ('genre', models.CharField(max_length=255)),
                ('ISBN', models.CharField(max_length=13)),
                ('language', models.CharField(max_length=255)),
                ('published_date', models.DateField()),
            ],
        ),
    ]