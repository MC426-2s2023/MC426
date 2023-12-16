# Generated by Django 4.2 on 2023-12-15 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0006_alter_locationprofile_user_lng'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locationprofile',
            name='user_lat',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='latitude'),
        ),
        migrations.AlterField(
            model_name='locationprofile',
            name='user_lng',
            field=models.DecimalField(decimal_places=6, max_digits=10, verbose_name='longitude'),
        ),
    ]