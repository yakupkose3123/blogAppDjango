# Generated by Django 4.0.4 on 2022-07-03 21:13

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0007_rename_profile_userprofile_alter_userprofile_options'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfile',
            new_name='Profile',
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
    ]
