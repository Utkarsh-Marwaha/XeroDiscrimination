# Generated by Django 2.2.4 on 2020-05-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='sex',
        ),
        migrations.AddField(
            model_name='user',
            name='pronoun',
            field=models.CharField(choices=[('they', 'they'), ('he', 'he'), ('she', 'she'), ('zie', 'zie'), ('hir', 'hir/hirs'), ('na', 'N/A')], default='they', max_length=32),
        ),
    ]
