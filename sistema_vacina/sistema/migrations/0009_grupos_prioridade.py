# Generated by Django 3.2.7 on 2021-09-15 18:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0008_auto_20210915_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupos_Prioridade',
            fields=[
                ('grupos_Prioridade', models.OneToOneField(choices=[('1', 'idoso'), ('2', 'Publico Geral'), ('3', 'Academicos de Saude'), ('4', 'Trabalhadores da linha de frente'), ('5', 'Pessoas com Comorbidade'), ('6', 'Gestantes e Lactantes de 18 a 59')], max_length=1, on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='sistema.paciente')),
            ],
        ),
    ]
