# Generated by Django 4.1.4 on 2022-12-29 02:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ecosite", "0005_alter_usuario_options_alter_usuario_managers_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="usuario",
            name="is_staff",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="is_superuser",
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name="usuario",
            name="telefone",
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
