# Generated by Django 2.2.10 on 2020-03-22 07:55

import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demo_module', '0006_auto_20200223_0900'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inbound_teststand_package',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Timestamp', models.CharField(blank=True, max_length=200, null=True)),
                ('NODELETE', models.BooleanField(default=False)),
                ('Sent_by', models.CharField(max_length=200)),
                ('command_list', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, null=True, size=None)),
                ('Validation_failed', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name_plural': 'Teststand packages',
            },
        ),
        migrations.CreateModel(
            name='ND_TS',
            fields=[
                ('ID', models.IntegerField(primary_key=True, serialize=False)),
                ('TimeStamp', models.CharField(blank=True, max_length=200, null=True)),
                ('NoDelete', models.BooleanField(default=False)),
                ('StatusCode', models.CharField(default='empty', max_length=50)),
            ],
            options={
                'verbose_name_plural': 'NoDelete & TimeStamp',
            },
        ),
        migrations.AlterModelOptions(
            name='status',
            options={'verbose_name_plural': 'Status'},
        ),
        migrations.CreateModel(
            name='Test_stand_parameters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parameter_name', models.CharField(default='Empty', max_length=100)),
                ('Parameter_value', models.CharField(default='Empty', max_length=100)),
                ('Inbound_teststand_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parameters', to='demo_module.Inbound_teststand_package')),
            ],
            options={
                'verbose_name_plural': 'Teststand parameters',
            },
        ),
        migrations.CreateModel(
            name='Test_stand_data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Data_name', models.CharField(max_length=100, null=True)),
                ('Data_points', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('Inbound_teststand_package', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='data', to='demo_module.Inbound_teststand_package')),
            ],
            options={
                'verbose_name_plural': 'Teststand data types',
            },
        ),
    ]
