# Generated by Django 2.2.1 on 2019-06-13 11:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='updates',
            new_name='updated',
        ),
    ]
