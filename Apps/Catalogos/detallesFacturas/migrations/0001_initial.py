# Generated by Django 4.2 on 2024-11-13 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbDetalledefactura',
            fields=[
                ('iddetallefactura', models.AutoField(db_column='IdDetalleFactura', primary_key=True, serialize=False)),
                ('nombretratamiento', models.CharField(db_collation='Modern_Spanish_CI_AS', db_column='NombreTratamiento', max_length=50)),
                ('precio', models.DecimalField(db_column='Precio', decimal_places=2, max_digits=10)),
            ],
            options={
                'db_table': 'Tb_DetalleDeFactura',
                'managed': False,
            },
        ),
    ]
