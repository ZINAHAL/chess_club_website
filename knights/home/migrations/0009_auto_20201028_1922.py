# Generated by Django 3.1.1 on 2020-10-28 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_auto_20201028_1845'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userinterfacepage',
            old_name='test',
            new_name='committee_and_coaches',
        ),
    ]