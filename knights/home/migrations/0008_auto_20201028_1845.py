# Generated by Django 3.1.1 on 2020-10-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userinterfacepage_sponsors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('group', models.CharField(choices=[('0', 'Committee'), ('1', 'Coaches'), ('2', 'Both')], max_length=1)),
                ('position', models.CharField(max_length=30)),
                ('image', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.RemoveField(
            model_name='userinterfacepage',
            name='benefactors',
        ),
        migrations.RemoveField(
            model_name='userinterfacepage',
            name='sponsors',
        ),
        migrations.AddField(
            model_name='userinterfacepage',
            name='test',
            field=models.ManyToManyField(to='home.Staff'),
        ),
    ]
