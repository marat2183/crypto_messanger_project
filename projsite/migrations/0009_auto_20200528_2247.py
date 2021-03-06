# Generated by Django 3.0.5 on 2020-05-28 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projsite', '0008_auto_20200528_2239'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='active',
            new_name='is_active',
        ),
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='login',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
