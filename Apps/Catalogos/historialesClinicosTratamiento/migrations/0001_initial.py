# Generated by Django 4.2 on 2024-11-13 22:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TbHistorialclinicotbTbTratamiento',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('precio', models.DecimalField(db_column='Precio', decimal_places=0, max_digits=18)),
            ],
            options={
                'db_table': 'Tb_HistorialClinicoTb_Tb_Tratamiento',
                'managed': False,
            },
        ),
    ]
