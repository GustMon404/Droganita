# Generated by Django 3.1.4 on 2020-12-22 02:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0007_auto_20201221_2308'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='encomenda',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='pedido',
            name='falta',
            field=models.BooleanField(),
        ),
    ]
