# Generated by Django 2.2.1 on 2019-05-02 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190502_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='pagamento',
            field=models.CharField(choices=[('p4', 'Parcelado em 4 vezes'), ('p3', 'Parcelado em 3 vezes'), ('p2', 'Parcelado em 2 vezes'), ('p5', 'Parcelado em 5 vezes'), ('av', 'Pagamento à vista')], default='av', max_length=2),
        ),
    ]