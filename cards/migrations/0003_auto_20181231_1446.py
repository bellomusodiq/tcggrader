# Generated by Django 2.1 on 2018-12-31 14:46

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('cards', '0002_card_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Album',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='category',
            new_name='album',
        ),
        migrations.RenameField(
            model_name='card',
            old_name='category',
            new_name='album',
        ),
    ]
