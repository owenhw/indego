# Generated by Django 3.1.7 on 2021-03-19 22:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Report',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250, unique=True)),
                ('title', models.CharField(max_length=40)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('fetched', models.BooleanField()),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
