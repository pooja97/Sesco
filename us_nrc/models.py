from django.db import models

# Create your models here.

class reactor_unit(models.Model):
    id = models.AutoField(primary_key=True)
    PlantName = models.CharField(max_length=500)
    DocketNumber = models.IntegerField(default=0)
    LicenseNumber = models.CharField(max_length=200)
    ReactorType = models.CharField(max_length=200)
    Location = models.CharField(max_length=500)
    Owner = models.CharField(max_length=200)
    NRC_Region = models.IntegerField(default=0)

class unit_report(models.Model):
    id = models.AutoField(primary_key=True)
    ReportDt = models.CharField(max_length = 300)
    Unit = models.CharField(max_length=200)
    Power = models.IntegerField(default=0)

class fact_table(models.Model):
    id = models.AutoField(primary_key=True)
    reactor_id = models.IntegerField(default = 0)
    report_id = models.IntegerField(default = 0)