# Generated by Django 2.0.7 on 2019-07-23 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='camara',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
                ('tipo', models.CharField(choices=[('digital,', 'Digital,'), ('reflex', 'Reflex')], default='digital', max_length=7)),
                ('megapixeles', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='minicomponente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modelo', models.CharField(max_length=50)),
                ('precio', models.IntegerField()),
                ('color', models.CharField(max_length=50)),
                ('peso', models.IntegerField()),
                ('potencia', models.CharField(max_length=50)),
                ('repro_usb', models.BooleanField()),
            ],
        ),
    ]
