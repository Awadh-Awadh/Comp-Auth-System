# Generated by Django 3.2.9 on 2021-11-11 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='user_name',
            new_name='username',
        ),
    ]