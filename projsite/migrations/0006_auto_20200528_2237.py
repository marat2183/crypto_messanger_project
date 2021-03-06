# Generated by Django 3.0.5 on 2020-05-28 19:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projsite', '0005_users_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='email',
            field=models.CharField(default='None', max_length=150, unique=True),
        ),
        migrations.AddField(
            model_name='users',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
