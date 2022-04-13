# Generated by Django 4.0.3 on 2022-04-13 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('photo_url', models.CharField(blank=True, default='', max_length=2000, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]