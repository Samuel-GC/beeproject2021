# Generated by Django 3.1.7 on 2021-05-10 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restbee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='add_data',
            old_name='piquera_abierta',
            new_name='piquera',
        ),
        migrations.RenameField(
            model_name='add_data',
            old_name='reina_dentro',
            new_name='reina',
        ),
    ]
