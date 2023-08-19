# Generated by Django 4.2.4 on 2023-08-17 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('revenue', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=25)),
                ('fuel', models.CharField(max_length=20)),
                ('consumption', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_sys.company')),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('phone', models.CharField(max_length=15)),
                ('gender', models.CharField(max_length=6)),
                ('distance', models.FloatField()),
                ('salary', models.FloatField()),
                ('animal', models.CharField(max_length=30)),
                ('bio', models.CharField(max_length=300)),
                ('company_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_sys.job')),
                ('vehicle_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company_sys.vehicle')),
            ],
        ),
    ]
