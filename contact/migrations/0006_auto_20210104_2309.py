# Generated by Django 3.1.3 on 2021-01-04 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0005_auto_20210104_2308'),
    ]

    operations = [
        migrations.DeleteModel(
            name='contacts',
        ),
        migrations.AlterField(
            model_name='contact',
            name='massage',
            field=models.TextField(max_length=700),
        ),
        migrations.AlterField(
            model_name='contact',
            name='subject',
            field=models.TextField(max_length=200),
        ),
    ]
