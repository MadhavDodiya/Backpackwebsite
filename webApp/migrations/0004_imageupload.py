# Generated by Django 5.0.6 on 2024-07-13 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webApp', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imageupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]