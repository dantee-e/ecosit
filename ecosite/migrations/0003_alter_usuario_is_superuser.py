# Generated by Django 4.1.3 on 2022-11-30 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecosite', '0002_usuario_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='is_superuser',
            field=models.BooleanField(default=True),
        ),
    ]