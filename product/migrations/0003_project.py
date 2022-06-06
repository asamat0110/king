# Generated by Django 4.1a1 on 2022-06-04 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Project_name', models.CharField(blank=True, max_length=255)),
                ('kinds', models.CharField(blank=True, db_index=True, max_length=255)),
                ('file', models.FileField(blank=True, upload_to='imeges/%Y/%m/%d')),
                ('context', models.TextField(blank=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
