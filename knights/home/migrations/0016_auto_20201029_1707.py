# Generated by Django 3.1.1 on 2020-10-29 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0015_homepagecontent_last_modified'),
    ]

    operations = [
        migrations.AddField(
            model_name='sponsor',
            name='display_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homepagecontent'),
        ),
        migrations.AddField(
            model_name='staff',
            name='display_page',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='home.homepagecontent'),
        ),
    ]