from django.db import models
# from clickhouse_backend import models

# Create your models here.


class reactor_unit(models.Model):   
    id = models.AutoField(primary_key=True)
    PlantName = models.CharField(max_length=200)
    DocketNumber = models.IntegerField(default=0)
    LicenseNumber = models.CharField(max_length=200)
    ReactorType = models.CharField(max_length=200)
    Location = models.CharField(max_length=500)
    State = models.CharField(max_length= 100,default='AK')
    Owner = models.CharField(max_length=200)
    NRC_Region = models.IntegerField(default=0)



class Report_data(models.Model):
    id = models.AutoField(primary_key=True)
    reactor = models.ForeignKey(reactor_unit,on_delete=models.CASCADE)
    ReportDt = models.DateField()
    ReportTime = models.CharField(max_length=200,default='12:00:00')
    ReportPeriod = models.CharField(max_length=100,default='AM')
    Unit = models.CharField(max_length = 200)
    Power = models.IntegerField(default=0)

    
    

