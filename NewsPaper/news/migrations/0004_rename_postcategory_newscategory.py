# Generated by Django 4.1.5 on 2023-02-12 17:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_subscription'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PostCategory',
            new_name='NewsCategory',
        ),
    ]
