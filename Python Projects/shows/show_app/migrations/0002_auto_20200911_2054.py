# Generated by Django 3.1.1 on 2020-09-11 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('show_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='release_date',
            field=models.DateField(null=True),
        ),
    ]
