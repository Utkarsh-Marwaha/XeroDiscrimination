# Generated by Django 2.2.4 on 2020-04-13 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_auto_20200412_2035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recommendations',
            name='email',
            field=models.EmailField(default='example@email.com', max_length=253),
        ),
    ]
