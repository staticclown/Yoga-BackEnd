# Generated by Django 5.0 on 2023-12-19 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserSignup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('signupname', models.CharField(max_length=30)),
                ('signuppassword', models.CharField(max_length=30)),
                ('signupdob', models.CharField(max_length=30)),
                ('signupemail', models.CharField(max_length=30)),
            ],
        ),
    ]
