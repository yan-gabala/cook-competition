# Generated by Django 3.2 on 2023-12-04 12:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='favorite',
            options={'default_related_name': 'recipe', 'ordering': ['user'], 'verbose_name': 'Избранное', 'verbose_name_plural': 'Избранное'},
        ),
    ]
