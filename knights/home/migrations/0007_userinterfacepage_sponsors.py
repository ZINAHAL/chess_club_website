# Generated by Django 3.1.1 on 2020-10-27 20:26

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_auto_20201027_1932'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinterfacepage',
            name='sponsors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(null=True, upload_to=''), default=list, size=None),
        ),
    ]