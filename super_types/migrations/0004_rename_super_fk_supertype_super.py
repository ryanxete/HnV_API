# Generated by Django 4.0.6 on 2022-07-18 22:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0003_supertype_super_fk'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supertype',
            old_name='super_fk',
            new_name='super',
        ),
    ]
