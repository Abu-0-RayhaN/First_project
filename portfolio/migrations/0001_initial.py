# Generated by Django 3.1.3 on 2021-01-29 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('link', models.CharField(max_length=30)),
                ('image', models.ImageField(upload_to='portfolio')),
            ],
        ),
    ]
