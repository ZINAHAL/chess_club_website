# Generated by Django 3.1.1 on 2020-10-28 19:45

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20201028_1922'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinterfacepage',
            name='benefactors',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=30), default=list, size=None),
        ),
    ]
