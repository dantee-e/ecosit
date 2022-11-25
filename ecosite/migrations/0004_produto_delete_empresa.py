# Generated by Django 4.1.3 on 2022-11-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecosite', '0003_delete_produto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('preco', models.FloatField()),
                ('loja', models.CharField(max_length=60)),
            ],
        ),
        migrations.DeleteModel(
            name='Empresa',
        ),
    ]
