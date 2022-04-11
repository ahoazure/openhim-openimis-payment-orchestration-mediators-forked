# Generated by Django 2.2 on 2021-12-19 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='configs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openimis_url', models.CharField(max_length=200, verbose_name='OpenIMIS URL')),
                ('openimis_port', models.IntegerField(verbose_name='Port')),
                ('openimis_user', models.CharField(max_length=200, verbose_name='User')),
                ('openimis_passkey', models.CharField(max_length=200, verbose_name='Password')),
                ('mifos_url', models.CharField(max_length=200, verbose_name='MiFOS URL')),
                ('mifos_port', models.IntegerField(verbose_name='Port')),
                ('mifos_user', models.CharField(max_length=200, verbose_name='User')),
                ('mifos_tenant', models.CharField(max_length=200, verbose_name='Tenant')),
                ('mifos_passkey', models.CharField(max_length=200, verbose_name='Password')),
                ('openhim_url', models.CharField(max_length=200, verbose_name='OpenHIM URL')),
                ('openhim_port', models.IntegerField(verbose_name='API Port')),
                ('openhim_user', models.CharField(max_length=200, verbose_name='Client Name')),
                ('openhim_passkey', models.CharField(max_length=200, verbose_name='Password')),
                ('mediator_url', models.CharField(max_length=200, verbose_name='Mediator URL')),
                ('mediator_port', models.IntegerField(verbose_name='Mediator Port')),
            ],
            options={
                'verbose_name': 'Configuration',
                'verbose_name_plural': 'Configurations',
                'db_table': 'mediator_configs',
                'managed': True,
            },
        ),
    ]
