# Generated by Django 3.1.1 on 2020-09-21 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ip_api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ipaddress',
            name='status',
            field=models.CharField(default='available', max_length=9),
            preserve_default=False,
        ),
    ]
