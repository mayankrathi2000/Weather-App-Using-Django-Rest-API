# Generated by Django 2.0.6 on 2018-06-10 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login_register', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='user',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]