# Generated by Django 3.0.7 on 2020-07-07 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admZone', '0002_auto_20200707_1150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.TextField()),
                ('notification', models.TextField()),
            ],
            options={
                'db_table': 'notification',
            },
        ),
    ]
