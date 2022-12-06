# Generated by Django 4.1.3 on 2022-11-30 16:00

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecosite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='username',
            field=models.CharField(default=0, error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
            preserve_default=False,
        ),
    ]