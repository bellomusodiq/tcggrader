# Generated by Django 2.1 on 2019-01-02 18:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0011_auto_20190102_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='link',
            field=models.URLField(max_length=1000),
        ),
    ]
