# Generated by Django 5.0.7 on 2024-07-13 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('user_name', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
