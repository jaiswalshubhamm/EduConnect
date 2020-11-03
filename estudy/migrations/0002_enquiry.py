# Generated by Django 3.0.7 on 2020-07-08 00:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('estudy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('mobno', models.CharField(max_length=50)),
                ('topic', models.CharField(max_length=50)),
                ('msg', models.TextField()),
            ],
            options={
                'db_table': 'enquiry',
            },
        ),
    ]
