# Generated by Django 5.0 on 2023-12-19 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorApp', '0003_rename_username_userlogin_useremail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersignup',
            name='id',
        ),
        migrations.AlterField(
            model_name='usersignup',
            name='signupemail',
            field=models.CharField(max_length=30, primary_key=True, serialize=False),
        ),
    ]
