from django.db import models

class IpAddress(models.Model):
    ip_address = models.CharField(max_length=12)
    status = models.CharField(max_length=9)