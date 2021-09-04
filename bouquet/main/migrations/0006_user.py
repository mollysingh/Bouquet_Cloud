# Generated by Django 3.2.4 on 2021-07-14 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_order_items'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=400)),
                ('last_name', models.CharField(max_length=400)),
                ('email', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12)),
                ('gender', models.CharField(max_length=22)),
                ('password', models.CharField(max_length=10)),
                ('confpwd', models.CharField(max_length=10)),
            ],
        ),
    ]
