# Generated by Django 2.2.4 on 2020-05-19 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200519_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='pronoun',
            field=models.CharField(choices=[('they', 'They/Them'), ('he', 'He/Him'), ('she', 'She/Her'), ('ot', 'Other'), ('na', 'Rather not say')], default='they', max_length=32),
        ),
    ]
