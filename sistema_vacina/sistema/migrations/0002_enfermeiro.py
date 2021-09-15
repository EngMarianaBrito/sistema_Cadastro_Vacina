# Generated by Django 3.2.7 on 2021-09-15 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enfermeiro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('coren', models.CharField(max_length=12, unique=True)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=60)),
            ],
        ),
    ]
