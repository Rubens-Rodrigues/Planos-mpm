# Generated by Django 5.0.1 on 2024-01-17 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_alter_order_date_payment_alter_person_date_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='document_number',
            field=models.CharField(default='', max_length=20, unique=True, verbose_name='Numero documento'),
        ),
    ]
