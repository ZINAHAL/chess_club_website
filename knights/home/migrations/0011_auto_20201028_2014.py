# Generated by Django 3.1.1 on 2020-10-28 20:14

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_userinterfacepage_benefactors'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinterfacepage',
            name='benefactors',
        ),
        migrations.AddField(
            model_name='userinterfacepage',
            name='sponsors_images',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.ImageField(null=True, upload_to=''), null=True, size=None),
        ),
    ]