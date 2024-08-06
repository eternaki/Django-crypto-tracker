# Generated by Django 3.2.8 on 2021-10-24 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crypto', '0005_auto_20211024_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='cryptopurchases',
            name='target_currency',
            field=models.CharField(default='EUR', max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cryptopurchases',
            name='target_price',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]
