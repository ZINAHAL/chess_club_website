# Generated by Django 3.1.1 on 2020-11-12 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0005_auto_20201112_1921'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PolicyDocument',
            new_name='Policy',
        ),
    ]
