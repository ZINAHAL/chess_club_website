# Generated by Django 3.1.1 on 2020-11-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0004_auto_20201112_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policydocument',
            name='document_name',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
