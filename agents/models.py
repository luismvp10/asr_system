# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Agent(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    host_name = models.CharField(max_length=20)
    community_name=models.CharField(max_length=30)
    ip_address = models.CharField(max_length=30)
    snmp_version = models.CharField(max_length=2)
    snmp_port = models.CharField(max_length=10)


    def __str__(self):
        return self.host_name