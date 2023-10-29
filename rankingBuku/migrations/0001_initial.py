# Generated by Django 4.2.6 on 2023-10-27 01:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared_models', '0002_load_fixtures'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ListBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('access', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=100)),
                ('description', models.TextField()),
                ('books', models.ManyToManyField(blank=True, related_name='list_books', to='shared_models.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]