# Generated by Django 2.2.4 on 2020-03-15 02:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post',
            new_name='company',
        ),
    ]