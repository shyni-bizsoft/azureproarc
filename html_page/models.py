# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Login(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=350)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'login'


class PsrMaster(models.Model):
    fromval = models.FloatField(blank=True, null=True)
    toval = models.FloatField(blank=True, null=True)
    chaptername = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    psr_rule = models.TextField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'psr_master'


class TrsMaster(models.Model):
    chapter_name = models.CharField(max_length=250, blank=True, null=True)
    hsn_code = models.CharField(max_length=250, blank=True, null=True)
    pdt_hsncode = models.CharField(max_length=250, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    unit = models.CharField(max_length=250, blank=True, null=True)
    year2006 = models.FloatField(blank=True, null=True)
    year2007 = models.FloatField(blank=True, null=True)
    year2008 = models.FloatField(blank=True, null=True)
    year2009 = models.FloatField(blank=True, null=True)
    year2010 = models.FloatField(blank=True, null=True)
    year2011 = models.FloatField(blank=True, null=True)
    year2012 = models.FloatField(blank=True, null=True)
    year2013 = models.FloatField(blank=True, null=True)
    year2014 = models.FloatField(blank=True, null=True)
    year2015 = models.FloatField(blank=True, null=True)
    year2016 = models.FloatField(blank=True, null=True)
    status = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'trs_master'
