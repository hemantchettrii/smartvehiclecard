# Generated by Django 3.0.8 on 2021-01-22 18:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='secondname',
            new_name='lastname',
        ),
    ]
