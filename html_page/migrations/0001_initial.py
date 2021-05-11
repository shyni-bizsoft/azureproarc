# Generated by Django 3.1.7 on 2021-04-24 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=250)),
                ('password', models.CharField(max_length=350)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'login',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TrsMaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chapter_name', models.CharField(blank=True, max_length=250, null=True)),
                ('hsn_code', models.CharField(blank=True, max_length=250, null=True)),
                ('pdt_hsncode', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('unit', models.CharField(blank=True, max_length=250, null=True)),
                ('year2006', models.FloatField(blank=True, null=True)),
                ('year2007', models.FloatField(blank=True, null=True)),
                ('year2008', models.FloatField(blank=True, null=True)),
                ('year2009', models.FloatField(blank=True, null=True)),
                ('year2010', models.FloatField(blank=True, null=True)),
                ('year2011', models.FloatField(blank=True, null=True)),
                ('year2012', models.FloatField(blank=True, null=True)),
                ('year2013', models.FloatField(blank=True, null=True)),
                ('year2014', models.FloatField(blank=True, null=True)),
                ('year2015', models.FloatField(blank=True, null=True)),
                ('year2016', models.FloatField(blank=True, null=True)),
                ('status', models.IntegerField()),
            ],
            options={
                'db_table': 'trs_master',
                'managed': False,
            },
        ),
    ]
