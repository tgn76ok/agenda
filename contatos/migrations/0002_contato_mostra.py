# Generated by Django 4.1.5 on 2023-01-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contato',
            name='mostra',
            field=models.BooleanField(default=True),
        ),
    ]
