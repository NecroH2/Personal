# Generated by Django 3.1.6 on 2021-02-18 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20210218_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuentau',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
