# Generated by Django 4.2.3 on 2023-07-19 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('position', models.CharField(max_length=255)),
                ('entry_date', models.CharField(max_length=10)),
                ('exit_date', models.CharField(max_length=10)),
                ('vacation_date', models.CharField(max_length=10)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employers', to='core.company')),
            ],
        ),
    ]
