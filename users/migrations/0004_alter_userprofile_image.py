# Generated by Django 4.0.4 on 2022-06-25 11:54

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_userprofile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='avatar.png', upload_to=users.models.user_profile_path),
        ),
    ]