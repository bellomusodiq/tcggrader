# Generated by Django 2.1 on 2019-01-02 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0010_auto_20190102_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='link',
            field=models.CharField(max_length=1000),
        ),
    ]
