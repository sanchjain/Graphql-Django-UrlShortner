# Generated by Django 3.1.1 on 2020-10-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='is_flagged',
            field=models.BooleanField(default=False),
        ),
    ]
