# Generated by Django 2.2 on 2022-03-24 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group_mediator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='group',
            options={'managed': True, 'ordering': ('id', 'name'), 'verbose_name': 'Group', 'verbose_name_plural': 'Groups'},
        ),
    ]