# Generated by Django 4.2.9 on 2024-05-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('ID', models.AutoField(primary_key=True, serialize=False)),
                ('Product', models.TextField(blank=True, null=True)),
                ('BuyerEmail', models.EmailField(blank=True, max_length=254, null=True)),
                ('PurchaseDate', models.DateField(blank=True, null=True)),
                ('Country', models.TextField(blank=True, null=True)),
                ('Price', models.FloatField(blank=True, null=True)),
                ('Refunded', models.CharField(choices=[('YES', 'Yes'), ('NO', 'No')], default='NO', max_length=20)),
                ('Currency', models.CharField(choices=[('USD', 'USD'), ('EUR', 'EUR')], default='USD', max_length=10)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]