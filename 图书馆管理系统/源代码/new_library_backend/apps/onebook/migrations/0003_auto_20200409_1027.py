# Generated by Django 2.1.4 on 2020-04-09 02:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onebook', '0002_auto_20200313_1218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onebook',
            name='bid',
            field=models.CharField(db_column='bid', default='', max_length=30),
        ),
    ]
