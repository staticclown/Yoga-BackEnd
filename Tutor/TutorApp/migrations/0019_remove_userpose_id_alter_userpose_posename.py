# Generated by Django 5.0.3 on 2024-03-21 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TutorApp', '0018_alter_userpose_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userpose',
            name='id',
        ),
        migrations.AlterField(
            model_name='userpose',
            name='poseName',
            field=models.CharField(max_length=70, primary_key=True, serialize=False),
        ),
    ]
