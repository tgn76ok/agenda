# Generated by Django 4.1.5 on 2023-01-24 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0002_contato_mostra'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='foro',
            field=models.ImageField(blank=True, upload_to='fotos/%y/%m/%d'),
        ),
    ]
