# Generated by Django 3.2.3 on 2021-05-25 19:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userbase',
            old_name='user_name',
            new_name='username',
        ),
    ]
