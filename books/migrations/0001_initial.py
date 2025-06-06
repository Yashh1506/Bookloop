# Generated by Django 5.0.1 on 2025-05-04 18:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('condition', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('category', models.CharField(default='Fiction', max_length=50)),
                ('tags', models.TextField()),
                ('language', models.CharField(default='English', max_length=20)),
                ('location', models.CharField(max_length=50)),
                ('exchange_option', models.CharField(default='Shipping', max_length=50)),
                ('coverimage', models.ImageField(upload_to='book_images/')),
                ('additional_image1', models.ImageField(upload_to='book_images/')),
                ('additional_image2', models.ImageField(upload_to='book_images/')),
                ('additional_image3', models.ImageField(upload_to='book_images/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
