# Generated by Django 2.2.9 on 2021-08-01 01:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Novo_Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data', models.DateTimeField(auto_now_add=True)),
                ('Nome', models.CharField(max_length=200)),
                ('Email', models.EmailField(max_length=250)),
                ('Telefone', models.CharField(max_length=14, validators=[django.core.validators.RegexValidator(message='Formato correto: (01)12345-6789 ou (01)2345-6789', regex='(\\(\\d{0,2}\\)\\d{4,5}\\-\\d{4})$')])),
                ('Endereco', models.CharField(max_length=250)),
            ],
        ),
    ]
