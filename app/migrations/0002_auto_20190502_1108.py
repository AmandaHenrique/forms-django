# Generated by Django 2.2.1 on 2019-05-02 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='pagamento',
            field=models.CharField(choices=[('av', 'Pagamento à vista'), ('p5', 'Parcelado em 5 vezes'), ('p2', 'Parcelado em 2 vezes'), ('p4', 'Parcelado em 4 vezes'), ('p3', 'Parcelado em 3 vezes')], default='av', max_length=2),
        ),
    ]
