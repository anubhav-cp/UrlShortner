# Generated by Django 3.2.4 on 2021-10-11 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortner', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='full_url',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(max_length=20),
        ),
    ]
