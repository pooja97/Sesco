# Generated by Django 4.2.5 on 2023-09-21 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("us_nrc", "0002_reactor_report"),
    ]

    operations = [
        migrations.CreateModel(
            name="reactor_units",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("PlantName_DocketNumber", models.CharField(max_length=500)),
                ("LicenseNumber", models.CharField(max_length=200)),
                ("ReactorType", models.CharField(max_length=200)),
                ("Location", models.CharField(max_length=500)),
                ("Owner", models.TextField(max_length=200)),
                ("NRC_Region", models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="unit_report",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("ReportDt", models.DateTimeField(verbose_name="Report datetime")),
                ("Unit", models.CharField(max_length=200)),
                ("Power", models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(name="power_reactor",),
        migrations.DeleteModel(name="reactor_report",),
    ]
