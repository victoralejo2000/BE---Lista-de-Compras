# Generated by Django 3.2 on 2023-11-02 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_producto_estado'),
    ]

    operations = [
        migrations.RenameField(
            model_name='producto',
            old_name='nombre',
            new_name='articulo',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='descripcion',
            new_name='detalle',
        ),
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
        migrations.AlterField(
            model_name='producto',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=12),
        ),
    ]
