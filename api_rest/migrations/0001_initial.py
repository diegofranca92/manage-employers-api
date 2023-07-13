# Generated by Django 4.2.3 on 2023-07-13 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_nickname', models.CharField(default='', max_length=100, primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=150)),
                ('user_email', models.EmailField(default='', max_length=254)),
            ],
        ),
    ]