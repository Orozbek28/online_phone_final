# Generated by Django 4.2 on 2023-05-11 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set(),
        ),
    ]
