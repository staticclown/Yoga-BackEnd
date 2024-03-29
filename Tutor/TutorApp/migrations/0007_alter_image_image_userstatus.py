# Generated by Django 4.2.2 on 2024-02-23 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TutorApp', '0006_remove_image_uploaded_at_alter_image_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(max_length=30000, upload_to='Userimages/'),
        ),
        migrations.CreateModel(
            name='UserStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginner', models.IntegerField(max_length=10)),
                ('level', models.IntegerField(max_length=10)),
                ('index', models.IntegerField(max_length=30)),
                ('mail_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TutorApp.usersignup')),
            ],
        ),
    ]
