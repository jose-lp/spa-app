# Generated by Django 3.1.2 on 2020-11-10 01:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointments', '0004_auto_20201109_0450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
