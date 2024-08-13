from django.db import models

# Create your models here.
class Address(models.Model):
    id = models.IntegerField(primary_key=True)
    city = models.CharField(max_length=10, blank=True, null=True)
    site_id = models.CharField(max_length=50, blank=True, null=True)
    road = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'address'