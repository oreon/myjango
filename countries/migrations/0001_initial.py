# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True, db_column=b'ID')),
                ('name', models.CharField(max_length=35, db_column=b'Name')),
                ('countrycode', models.CharField(max_length=3, db_column=b'CountryCode')),
                ('district', models.CharField(max_length=20, db_column=b'District')),
                ('population', models.IntegerField(db_column=b'Population')),
            ],
            options={
                'db_table': 'city',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('code', models.CharField(max_length=3, serialize=False, primary_key=True, db_column=b'Code')),
                ('name', models.CharField(max_length=52, db_column=b'Name')),
                ('continent', models.CharField(max_length=13, db_column=b'Continent')),
                ('region', models.CharField(max_length=26, db_column=b'Region')),
                ('surfacearea', models.FloatField(db_column=b'SurfaceArea')),
                ('indepyear', models.IntegerField(null=True, db_column=b'IndepYear', blank=True)),
                ('population', models.IntegerField(db_column=b'Population')),
                ('lifeexpectancy', models.FloatField(null=True, db_column=b'LifeExpectancy', blank=True)),
                ('gnp', models.FloatField(null=True, db_column=b'GNP', blank=True)),
                ('gnpold', models.FloatField(null=True, db_column=b'GNPOld', blank=True)),
                ('localname', models.CharField(max_length=45, db_column=b'LocalName')),
                ('governmentform', models.CharField(max_length=45, db_column=b'GovernmentForm')),
                ('headofstate', models.CharField(max_length=60, db_column=b'HeadOfState', blank=True)),
                ('capital', models.IntegerField(null=True, db_column=b'Capital', blank=True)),
                ('code2', models.CharField(max_length=2, db_column=b'Code2')),
            ],
            options={
                'db_table': 'country',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Countrylanguage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('countrycode', models.CharField(max_length=3, db_column=b'CountryCode')),
                ('language', models.CharField(max_length=30, db_column=b'Language')),
                ('isofficial', models.CharField(max_length=1, db_column=b'IsOfficial')),
                ('percentage', models.FloatField(db_column=b'Percentage')),
            ],
            options={
                'db_table': 'countrylanguage',
            },
            bases=(models.Model,),
        ),
    ]
