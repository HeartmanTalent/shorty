# Generated by Django 2.1.15 on 2021-05-24 16:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0003_auto_20210523_2234'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='short',
            unique_together={('long_url', 'user')},
        ),
    ]
