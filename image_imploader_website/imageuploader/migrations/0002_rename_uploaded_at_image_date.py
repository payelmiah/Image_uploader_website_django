# Generated by Django 5.1.5 on 2025-02-02 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('imageuploader', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='uploaded_at',
            new_name='date',
        ),
    ]
