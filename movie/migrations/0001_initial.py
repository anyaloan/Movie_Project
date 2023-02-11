# Generated by Django 4.1.5 on 2023-01-14 08:51

from django.db import migrations, models
import movie.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('description', models.TextField(blank=True, null=True)),
                ('duration', models.FloatField()),
                ('rate', models.FloatField()),
                ('year', models.FloatField()),
                ('date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, upload_to=movie.models.upload_news_image)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
    ]
