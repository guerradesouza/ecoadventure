# Generated by Django 5.0.7 on 2024-08-06 01:45

import core.models
import stdimage.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_servico_imagem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servico',
            name='icone',
            field=models.CharField(choices=[('bi bi-gear', 'Engrenagem'), ('ini-stats-up', 'Gráfico'), ('ini-users', 'Usuários'), ('ini-layers', 'Design'), ('ini-mobile', 'Mobile'), ('ini-rocket', 'Foguete')], max_length=24, verbose_name='Ícone'),
        ),
        migrations.AlterField(
            model_name='servico',
            name='imagem',
            field=stdimage.models.StdImageField(force_min_size=False, upload_to=core.models.get_file_path, variations={'thumb': {'crop': True, 'height': 80, 'width': 80}}, verbose_name='Imagem'),
        ),
    ]
