# Generated by Django 4.0.6 on 2022-07-18 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0005_remove_supertype_super'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.supertype'),
        ),
    ]
