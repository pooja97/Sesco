# Generated by Django 4.2.5 on 2023-09-27 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("us_nrc", "0022_alter_report_data_reactor"),
    ]

    operations = [
        migrations.AddField(
            model_name="report_data",
            name="ReportPeriod",
            field=models.CharField(default="AM", max_length=100),
        ),
        migrations.AddField(
            model_name="report_data",
            name="ReportTime",
            field=models.CharField(default="12:00:00", max_length=200),
        ),
    ]
