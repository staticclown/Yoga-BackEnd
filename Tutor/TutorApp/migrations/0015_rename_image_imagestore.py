# Generated by Django 4.2.2 on 2024-02-26 15:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('TutorApp', '0014_index_level'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='ImageStore',
        ),
    ]