# Generated by Django 3.1.1 on 2020-10-27 12:29

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_userinterfacepage_summary_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=20)),
                ('fullname', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='userinterfacepage',
            name='benefactors',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), default=[], size=20),
        ),
    ]
