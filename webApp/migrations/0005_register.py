# Generated by Django 5.0.6 on 2024-07-13 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0004_imageupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]