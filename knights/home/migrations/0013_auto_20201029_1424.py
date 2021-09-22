# Generated by Django 3.1.1 on 2020-10-29 14:24

from django.db import migrations, models
import django_better_admin_arrayfield.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_auto_20201028_2059'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinterfacepage',
            name='club_sponsors',
        ),
        migrations.RemoveField(
            model_name='userinterfacepage',
            name='committee_and_coaches',
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='company_name',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='staff',
            name='fullname',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='staff',
            name='group',
            field=models.CharField(choices=[('0', 'Committee'), ('1', 'Coaches')], max_length=1),
        ),
        migrations.AlterField(
            model_name='staff',
            name='position',
            field=models.CharField(max_length=70),
        ),
        migrations.AlterField(
            model_name='userinterfacepage',
            name='benefactors',
            field=django_better_admin_arrayfield.models.fields.ArrayField(base_field=models.CharField(max_length=70), default=list, size=None),
        ),
    ]
